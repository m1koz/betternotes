# -*- coding: utf-8 -*-
"""
Renders the BetterNotes quill mark to PNG / ICO with no third-party deps.

The mark is an SVG path (lines and cubic curves) stroked with round caps and
joins. Curves are flattened into short segments; because a capsule (the set
of points within r of a segment) is convex, its intersection with any
horizontal line is a single interval - so we can scan-convert exactly, per
row, instead of testing every pixel. Anti-aliasing comes from 4x vertical
supersampling plus exact fractional coverage at the horizontal ends.
"""
import io, os, struct, zlib, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), 'src')

# The mark in a 100x100 box: a quill pen - the vane as two curves meeting at
# the tip, the shaft running through it down to the nib, and a drop of ink
# below. Four subpaths, one colour, stroke 9. The same string lives in
# src/index.html (#splashS) and in IC.logo in src/js/05-core.js; keep the
# three identical.
PATH_D = 'M84 12 C86 46 68 74 32 78 M84 12 C46 20 30 44 34 62 M84 12 C60 36 40 60 18 90 M8 96 L9 96'
STROKE = 9.0


def flatten(d, step=0.8):
    """Absolute M/L/H/V/C/Z path data -> list of polylines, one per subpath."""
    for ch in 'MLHVCZ':
        d = d.replace(ch, ' ' + ch + ' ')
    toks = d.split()
    subs, cur, pos, start, cmd = [], [], None, None, None
    i = 0

    def num():
        nonlocal i
        v = float(toks[i]); i += 1
        return v

    while i < len(toks):
        if toks[i] in 'MLHVCZ':
            cmd = toks[i]; i += 1
        if cmd == 'M':
            if cur:
                subs.append(cur)
            pos = (num(), num()); start = pos; cur = [pos]; cmd = 'L'
        elif cmd == 'L':
            pos = (num(), num()); cur.append(pos)
        elif cmd == 'H':
            pos = (num(), pos[1]); cur.append(pos)
        elif cmd == 'V':
            pos = (pos[0], num()); cur.append(pos)
        elif cmd == 'C':
            c1 = (num(), num()); c2 = (num(), num()); p1 = (num(), num())
            p0 = pos
            ln = math.dist(p0, c1) + math.dist(c1, c2) + math.dist(c2, p1)
            n = max(4, int(ln / step))
            for k in range(1, n + 1):
                t = k / n; u = 1 - t
                cur.append((u*u*u*p0[0] + 3*u*u*t*c1[0] + 3*u*t*t*c2[0] + t*t*t*p1[0],
                            u*u*u*p0[1] + 3*u*u*t*c1[1] + 3*u*t*t*c2[1] + t*t*t*p1[1]))
            pos = p1
        elif cmd == 'Z':
            cur.append(start); pos = start
            subs.append(cur); cur = []; cmd = None
    if cur:
        subs.append(cur)
    return subs


SUBPATHS = flatten(PATH_D)
PTS = [p for sub in SUBPATHS for p in sub]     # bounding box source


def row_interval(ax, ay, bx, by, r, y):
    """[x0, x1] where the capsule around AB meets the horizontal line at y."""
    lo, hi = None, None

    for (cx, cy) in ((ax, ay), (bx, by)):                 # the two round caps
        dy = y - cy
        if abs(dy) <= r:
            hw = math.sqrt(r * r - dy * dy)
            l, h = cx - hw, cx + hw
            lo = l if lo is None else min(lo, l)
            hi = h if hi is None else max(hi, h)

    dx, dy = bx - ax, by - ay                             # the rectangular body
    ln = math.hypot(dx, dy)
    if ln > 1e-9:
        nx, ny = -dy / ln * r, dx / ln * r
        quad = [(ax + nx, ay + ny), (bx + nx, by + ny), (bx - nx, by - ny), (ax - nx, ay - ny)]
        for i in range(4):
            x1, y1 = quad[i]
            x2, y2 = quad[(i + 1) % 4]
            if (y1 <= y < y2) or (y2 <= y < y1):
                t = (y - y1) / (y2 - y1)
                x = x1 + (x2 - x1) * t
                lo = x if lo is None else min(lo, x)
                hi = x if hi is None else max(hi, x)

    if lo is None:
        return None
    return (lo, hi)


def render_mask(size, scale, offx, offy, pts=None, samples=4):
    """Grayscale coverage of a polyline, as a list of floats, size*size long."""
    pts = PTS if pts is None else pts
    r = STROKE * 0.5 * scale
    segs = []
    for i in range(len(pts) - 1):
        ax, ay = pts[i]
        bx, by = pts[i + 1]
        segs.append((ax * scale + offx, ay * scale + offy,
                     bx * scale + offx, by * scale + offy))

    cov = [0.0] * (size * size)
    w = 1.0 / samples

    for py in range(size):
        row = cov[py * size:(py + 1) * size]
        hit = False
        for s in range(samples):
            y = py + (s + 0.5) * w
            spans = []
            for (ax, ay, bx, by) in segs:
                iv = row_interval(ax, ay, bx, by, r, y)
                if iv:
                    spans.append(iv)
            if not spans:
                continue
            spans.sort()
            merged = [list(spans[0])]                      # union, so overlaps
            for lo, hi in spans[1:]:                       # are not double-counted
                if lo <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], hi)
                else:
                    merged.append([lo, hi])
            for lo, hi in merged:
                lo = max(0.0, lo); hi = min(float(size), hi)
                if hi <= lo:
                    continue
                hit = True
                i0, i1 = int(lo), int(math.ceil(hi))
                for px in range(i0, min(i1, size)):
                    l = max(lo, px); h = min(hi, px + 1.0)
                    if h > l:
                        row[px] += (h - l) * w
        if hit:
            cov[py * size:(py + 1) * size] = row
    return cov


BG = (7, 9, 12)
FG = (243, 240, 234)


def rrect_alpha(x, y, size, body, radius):
    """Покрытие точки (x, y) скруглённым квадратом со стороной body и углом
    radius, стоящим по центру холста size. Сглаживание — по расстоянию до
    границы: одна пиксельная ширина перехода."""
    half = body / 2.0
    cx, cy = size / 2.0, size / 2.0
    dx = abs(x - cx) - (half - radius)
    dy = abs(y - cy) - (half - radius)
    if dx <= 0 and dy <= 0:
        d = max(dx, dy) - radius           # внутри: отрицательное расстояние
    else:
        d = math.hypot(max(dx, 0.0), max(dy, 0.0)) - radius
    a = 0.5 - d
    return 0.0 if a <= 0 else (1.0 if a >= 1 else a)


def icon_rgba(size, inset=0.60, body=1.0, corner=0.0):
    """Знак одним цветом на плотном фоне. body < 1 оставляет прозрачные поля
    вокруг скруглённой плитки — так устроены иконки macOS: плитка 824/1024
    с углом 22 %, поля прозрачные."""
    xs = [q[0] for q in PTS]
    ys = [q[1] for q in PTS]
    span = max(max(xs) - min(xs), max(ys) - min(ys)) + STROKE
    scale = size * body * inset / span
    offx = size / 2.0 - (min(xs) + max(xs)) / 2.0 * scale
    offy = size / 2.0 - (min(ys) + max(ys)) / 2.0 * scale

    cov = [0.0] * (size * size)
    for sub in SUBPATHS:                                   # union of subpaths
        part = render_mask(size, scale, offx, offy, pts=sub)
        cov = [min(1.0, a + b) for a, b in zip(cov, part)]
    tile = size * body
    radius = tile * corner
    out = bytearray(size * size * 4)
    for py in range(size):
        for px in range(size):
            i = py * size + px
            a = cov[i]
            alpha = 1.0 if body >= 1.0 else rrect_alpha(px + 0.5, py + 0.5, size, tile, radius)
            out[i * 4 + 0] = int(BG[0] + (FG[0] - BG[0]) * a)
            out[i * 4 + 1] = int(BG[1] + (FG[1] - BG[1]) * a)
            out[i * 4 + 2] = int(BG[2] + (FG[2] - BG[2]) * a)
            out[i * 4 + 3] = int(round(255 * alpha))
    return bytes(out)


def png_bytes(size, rgba):
    def chunk(tag, data):
        c = struct.pack('>I', len(data)) + tag + data
        return c + struct.pack('>I', zlib.crc32(tag + data) & 0xFFFFFFFF)
    raw = b''.join(b'\x00' + rgba[y * size * 4:(y + 1) * size * 4] for y in range(size))
    return (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9))
            + chunk(b'IEND', b''))


def ico_bytes(pngs):
    """pngs: [(size, png_bytes)] - Vista+ ICO with embedded PNG frames."""
    head = struct.pack('<HHH', 0, 1, len(pngs))
    offset = 6 + 16 * len(pngs)
    entries, blobs = b'', b''
    for size, data in pngs:
        s = 0 if size >= 256 else size
        entries += struct.pack('<BBBBHHII', s, s, 0, 0, 1, 32, len(data), offset)
        blobs += data
        offset += len(data)
    return head + entries + blobs


def main():
    made = []
    for size, name, inset in ((512, 'icon-512.png', 0.66),):
        rgba = icon_rgba(size, inset)
        p = os.path.join(OUT, name)
        with open(p, 'wb') as f:
            f.write(png_bytes(size, rgba))
        made.append(name)
        print('  %-22s %d x %d' % (name, size, size))

    # исходник для иконок нативной оболочки (cargo tauri icon): плитка macOS
    # с прозрачными полями, 1024 px
    tauri_icons = os.path.join(os.path.dirname(HERE), 'src-tauri', 'icons')
    if os.path.isdir(tauri_icons):
        p = os.path.join(tauri_icons, 'source.png')
        with open(p, 'wb') as f:
            f.write(png_bytes(1024, icon_rgba(1024, 0.66, body=0.805, corner=0.225)))
        print('  %-22s 1024 x 1024 (src-tauri/icons/source.png)' % 'source.png')

    frames = []
    for s in (16, 32, 48, 64, 128, 256):
        frames.append((s, png_bytes(s, icon_rgba(s, 0.72))))
    with open(os.path.join(OUT, 'favicon.ico'), 'wb') as f:
        f.write(ico_bytes(frames))
    print('  %-22s 16/32/48/64/128/256' % 'favicon.ico')

    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
           '<rect width="100" height="100" rx="22" fill="#07090C"/>'
           '<path d="' + PATH_D + '" fill="none" stroke="#F3F0EA" '
           'stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    with open(os.path.join(OUT, 'icon.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)
    print('  %-22s vector' % 'icon.svg')


if __name__ == '__main__':
    print('Rendering BetterNotes icons ->', OUT)
    main()
    print('Done.')
