<p align="center">
  <img src="assets/hero.jpg" width="960" alt="BetterNotes — notes, projects, plans and a week calendar">
</p>

<h1 align="center">BetterNotes</h1>

<p align="center">
  Notes, projects, plans and a week calendar — in one window, on your computer.<br>
  No account, no cloud, no subscription. Your data is a folder of ordinary files.
</p>

<p align="center">
  <a href="https://github.com/m1koz/betternotes/releases/latest"><img src="https://img.shields.io/github/v/release/m1koz/betternotes?display_name=tag&color=F2A85C&label=download" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/macOS-11%2B-000000?logo=apple&logoColor=white" alt="macOS 11+">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4?logo=windows&logoColor=white" alt="Windows 10 / 11">
  <img src="https://img.shields.io/badge/license-freeware-8E8E93" alt="Freeware">
</p>

<p align="center">
  <a href="https://github.com/m1koz/betternotes/releases/latest/download/BetterNotes-macos.dmg"><b>⬇ Download for macOS</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/m1koz/betternotes/releases/latest/download/BetterNotes-windows-setup.exe"><b>⬇ Download for Windows</b></a>
</p>

## Why

Most note apps want an account, a sync server and a monthly fee — and then your notes live somewhere else. BetterNotes runs entirely on your machine. Everything you write lands in a `data/` folder next to the app as plain files: copy the folder and you have a backup, put it in iCloud Drive or OneDrive and it travels with you, move the app to another disk and it keeps working.

It is one window with five sections: **Home**, **Plans**, **Calendar**, **Notes** and **Projects** — the things you do today on the left, the things that accumulate on the right.

## Download

| | Recommended | Also available |
|---|---|---|
| **macOS 11+** (Apple silicon & Intel) | [`BetterNotes-macos.dmg`](https://github.com/m1koz/betternotes/releases/latest/download/BetterNotes-macos.dmg) — open, drag to Applications | [`BetterNotes-macos.zip`](https://github.com/m1koz/betternotes/releases/latest/download/BetterNotes-macos.zip) — the `.app` itself, unzip anywhere |
| **Windows 10 / 11** | [`BetterNotes-windows-setup.exe`](https://github.com/m1koz/betternotes/releases/latest/download/BetterNotes-windows-setup.exe) — the installer, adds Start menu and uninstall entries | [`BetterNotes-windows.zip`](https://github.com/m1koz/betternotes/releases/latest/download/BetterNotes-windows.zip) — portable, keeps its data next to the `.exe` |

All builds are on the [Releases](https://github.com/m1koz/betternotes/releases) page and in the [`dist/`](dist) folder of this repository. On a Mac take the `.dmg`, on Windows the `-setup.exe`.

To verify a download:

```bash
shasum -a 256 -c BetterNotes-macos.dmg.sha256
```

> **macOS:** the app is distributed outside the App Store and is not notarized, so the first launch may say *"BetterNotes cannot be opened"*. Open **System Settings → Privacy & Security** and click **Open Anyway**, or run once in Terminal:
> ```bash
> xattr -dr com.apple.quarantine /Applications/BetterNotes.app
> ```
>
> **Windows:** SmartScreen may show *"Windows protected your PC"* because the installer is not signed with a paid certificate yet. Click **More info → Run anyway**. The installer is built automatically from the same code as the macOS app and contains nothing but the app.

## What's inside

### Notes
Rich text with headings, lists and checklists, pictures you resize with the mouse, tags, comments and pinning. A note can live on its own or inside a project.

<p align="center"><img src="assets/note.png" width="860" alt="A note with a picture and a checklist"></p>

### Calendar
A week by hours. Click a free slot to create an event, give it a description and a color, drag it to another time or day, pull the bottom edge to make it longer. Task deadlines and daily goals show up in the *all day* strip.

<p align="center"><img src="assets/calendar.png" width="860" alt="Week calendar with colored events"></p>

### Projects
Tasks with deadlines, and inside each task its own notes, links and files. Every project has a file explorer with folders and drag-and-drop, a photo wall, links, a discussion thread and progress.

<p align="center"><img src="assets/project-tasks.png" width="860" alt="Project tasks"></p>
<p align="center"><img src="assets/project-files.png" width="860" alt="Project files"></p>

### Plans
Goals by day, week, month and year. A goal breaks down into the periods inside it; progress rolls up from the bottom, so ticking off a day moves the week, the month and the year. Pick two dates and BetterNotes chooses the horizon for you. Log what you did each day and turn the log into a report note with one click.

<p align="center"><img src="assets/plans.png" width="860" alt="Plans for the week"></p>

### Home and search
Home greets you by name and gathers what is coming up: goals, today's events, pinned notes and active projects. **⌘K / Ctrl+K** searches everything — notes, tasks, events, goals, links, and the contents of text files you attached.

<p align="center"><img src="assets/home.png" width="860" alt="Home"></p>
<p align="center"><img src="assets/search.png" width="860" alt="Search palette"></p>

### Dark or light, in ten languages
Two themes that follow the system or your choice. The interface is available in English, Русский, Українська, Deutsch, Français, Español, Italiano, Português, 中文 and 日本語; on first launch BetterNotes takes the language of your system.

<p align="center"><img src="assets/light-calendar.png" width="860" alt="Light theme"></p>

## Your data

```
data/
  betternotes.json   notes, projects, plans, events, settings
  blobs/             attachments — photos and files, as they are
  text/              text of attached files, for search
  backups/           copies the app writes on its own
```

- **Where:** next to the app, if that folder is writable. Apps installed into `/Applications` or `Program Files` keep their data in the user folder instead; the exact path is always shown in **Settings → Data**, with *Open data folder* and *Move…* buttons.
- **Backups:** a daily copy without attachments and a weekly one with everything, 30 and 8 kept. **Settings → Backups** makes a copy right now, restores any of them, opens the folder.
- **Moving between computers:** *Export to file* on one, *Import from file* on the other — Mac or Windows, it does not matter. Or just copy the `data` folder.
- **No network.** BetterNotes never opens a connection. The only thing it downloads is nothing.

## Keyboard shortcuts

| | |
|---|---|
| `⌘K` / `Ctrl+K` | search |
| `⌘N` / `Ctrl+N` | new note |
| `1` … `5` | sections |
| `←` / `→` | previous / next week in the calendar |
| `Esc` | back / close |
| `⌘↩` / `Ctrl+Enter` | send a comment |
| right-click | card menu |
| click a picture | select; drag the corner to resize, `Shift` for free aspect, `Alt+←/→` by 10 %, double-click for original |

The full list is in **Settings → Keyboard shortcuts**.

## Built with

<p>
  <img src="https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/Tauri%202-24C8D8?logo=tauri&logoColor=white" alt="Tauri 2">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
</p>

BetterNotes is a native app written in **Rust** on [Tauri 2](https://tauri.app): the window, the `data/` folder, attachments, backups, system dialogs and file opening all live in the Rust core, and the interface is compiled into the same binary — no framework, no bundler, no runtime to install. The icon and installer artwork are generated by **Python** scripts with nothing but the standard library. One code base, a 5 MB binary, macOS and Windows builds from the same commit.

What is in this repository: the releases (`dist/`), the screenshots (`assets/`) and the icon and installer-art generators (`tools/`). The application code itself is not published.

## FAQ

**Is it free?** Yes. No trial, no in-app purchases, no telemetry.

**Where is the source?** BetterNotes is freeware, not open source. This repository holds the releases, the documentation and the build tooling — not the application code.

**Does it sync?** Not yet. Put the `data` folder in iCloud Drive, OneDrive or any synced folder and it will follow you; real device-to-device sync is on the roadmap.

**How do I update?** Download the new build and replace the app. Your notes live in the `data` folder, not inside the app, so nothing is lost — but a backup before an update never hurts (**Settings → Backups → Back up now**).

**Can I change the font?** The app ships with the system font. If you own *TT Norms Pro*, BetterNotes will pick it up — see **Settings → About**.

**Something broke.** Open an [issue](https://github.com/m1koz/betternotes/issues) or write to [t.me/mkships](https://t.me/mkships).

## License

BetterNotes is free to download and use under the [End User License Agreement](LICENSE). © 2026 m1koz. All rights reserved.
