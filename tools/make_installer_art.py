# -*- coding: utf-8 -*-
"""
Картинки для установщика Windows (NSIS), без сторонних библиотек:

  src-tauri/icons/nsis-header.bmp   150×57  — знак на белом, в шапке страниц
  src-tauri/icons/nsis-sidebar.bmp  164×314 — тёмная боковая панель с пером
                                              и янтарным свечением

NSIS понимает только несжатый 24-битный BMP. Знак берётся из make_icons.py,
поэтому при смене логотипа хватит одного запуска обоих скриптов.
"""
import os, struct, math
import make_icons as mi

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(os.path.dirname(HERE), 'src-tauri', 'icons')


def bmp_bytes(w, h, rgb):
    """24-битный BMP: строки снизу вверх, BGR, выравнивание строки на 4 байта."""
    row = (w * 3 + 3) // 4 * 4
    pixels = bytearray()
    for y in range(h - 1, -1, -1):
        line = bytearray()
        for x in range(w):
            r, g, b = rgb[y * w + x]
            line += bytes((b, g, r))
        line += b'\0' * (row - w * 3)
        pixels += line
    header = struct.pack('<2sIHHI', b'BM', 54 + len(pixels), 0, 0, 54)
    info = struct.pack('<IiiHHIIiiII', 40, w, h, 1, 24, 0, len(pixels), 2835, 2835, 0, 0)
    return header + info + bytes(pixels)


def mark_coverage(w, h, cx, cy, box):
    """Покрытие знака (0..1) в квадрате box×box с центром (cx, cy) на холсте w×h."""
    xs = [q[0] for q in mi.PTS]
    ys = [q[1] for q in mi.PTS]
    span = max(max(xs) - min(xs), max(ys) - min(ys)) + mi.STROKE
    scale = box / span
    size = max(w, h)
    offx = cx - (min(xs) + max(xs)) / 2.0 * scale
    offy = cy - (min(ys) + max(ys)) / 2.0 * scale
    cov = [0.0] * (size * size)
    for sub in mi.SUBPATHS:
        part = mi.render_mask(size, scale, offx, offy, pts=sub)
        cov = [min(1.0, a + b) for a, b in zip(cov, part)]
    return [cov[y * size + x] for y in range(h) for x in range(w)]


def mix(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def header():
    w, h = 150, 57
    white, ink = (255, 255, 255), (27, 26, 24)
    cov = mark_coverage(w, h, w - 30, h / 2.0, 34)
    rgb = [mix(white, ink, c) for c in cov]
    return bmp_bytes(w, h, rgb)


def sidebar():
    w, h = 164, 314
    top, bottom = (16, 17, 22), (10, 11, 14)
    amber, paper = (242, 168, 92), (239, 236, 230)
    cov = mark_coverage(w, h, w / 2.0, 118, 78)
    rgb = []
    for y in range(h):
        base = mix(top, bottom, y / float(h - 1))
        for x in range(w):
            # мягкое свечение позади знака
            d = math.hypot((x - w / 2.0) / 70.0, (y - 118) / 62.0)
            glow = max(0.0, 1.0 - d) ** 2 * 0.55
            px = mix(base, amber, glow)
            rgb.append(mix(px, paper, cov[y * w + x]))
    return bmp_bytes(w, h, rgb)


def main():
    with open(os.path.join(ICONS, 'nsis-header.bmp'), 'wb') as f:
        f.write(header())
    with open(os.path.join(ICONS, 'nsis-sidebar.bmp'), 'wb') as f:
        f.write(sidebar())
    print('nsis-header.bmp 150x57, nsis-sidebar.bmp 164x314')


if __name__ == '__main__':
    main()
