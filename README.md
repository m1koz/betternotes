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
> **Windows:** SmartScreen may show *"Windows protected your PC"* because the installer is not signed with a paid certificate yet. Click **More info → Run anyway**. The installer is built from the same application code as the macOS app.

## What's inside

### Notes
Rich text with headings, lists and checklists, pictures you resize with the mouse, tags, comments and pinning. Highlight important passages with presets or any custom colour, or change the text colour. Colour stops at the end of the highlighted passage when you continue typing. **Remove colour** clears the selected text colour and highlight while keeping bold, italic and other formatting. A note can live on its own, in a project, or in a project branch.

<p align="center"><img src="assets/note.png" width="860" alt="A note with a picture and a checklist"></p>
<p align="center"><img src="assets/highlights.jpg" width="860" alt="Custom text highlights in a learning journal"></p>

### Calendar
A week by hours. Click a free slot to create an event, give it a description and a color, drag it to another time or day, pull the bottom edge to make it longer. Task deadlines and daily goals show up in the *all day* strip.

<p align="center"><img src="assets/calendar.png" width="860" alt="Week calendar with colored events"></p>

### Projects
Tasks with deadlines, and inside each task its own notes, links and files. Every project has a file explorer with folders and drag-and-drop, a photo wall, links, a discussion thread and progress.

The **Branches** tab, right after **Overview**, splits a project into topics with their own tasks, notes, folders, files and links. Add nested branches when a topic needs more structure. Each branch can optionally contribute its tasks to project progress; deadlines still appear in Plans and Calendar. Search, export and full backups include branch contents.

<p align="center"><img src="assets/branches.jpg" width="860" alt="Project branches after the Overview tab"></p>
<p align="center"><img src="assets/nested-branches.jpg" width="860" alt="Nested topics with independent progress settings"></p>

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

## Updates and app removal

Open **Settings → Update and removal → Check for updates** to install the latest release. BetterNotes verifies the update signature, saves a safety copy of the app and data, and restarts after installation. Notes, projects, branches and attachments stay in place.

**Remove app** in the same section removes the application and closes it. Your data and backups remain available if you reinstall. On macOS the app goes to the Trash; on Windows an installed copy uses its uninstaller, and a portable copy goes to the Recycle Bin.

<p align="center"><img src="assets/maintenance.jpg" width="860" alt="Settings with update and app removal controls"></p>

Versions before 1.2.1 need one manual update to get these controls.

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
- **Local data.** Notes and attachments stay on your computer. The app works offline; an optional fallback font may load from Google Fonts when online. Checking for updates contacts this GitHub repository and sends no notes or attachments.

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

BetterNotes uses **Rust** and [Tauri 2](https://tauri.app) for the native window, file storage, attachments, backups and system dialogs on both macOS and Windows. The interface uses **JavaScript, HTML and CSS** in the system WebView and is embedded in the application binary. **Python** is used for development tools and artwork generation; users do not need Python or npm.

This repository contains ready-to-use applications (`dist/`), screenshots (`assets/`), release notes and the license. The application source is not published.

## FAQ

**Is it free?** Yes. No trial, no in-app purchases, no telemetry.

**Where is the source?** BetterNotes is freeware, not open source. This repository holds ready-to-use releases, screenshots and documentation. The application source is not published.

**Why does GitHub show “Source code” downloads?** GitHub generates ZIP/TAR archives of every tagged repository automatically. Here they contain the distribution files and documentation, not the application source. Use the recommended installers above.

**Does it sync?** Not yet. Put the `data` folder in iCloud Drive, OneDrive or any synced folder and it will follow you; real device-to-device sync is on the roadmap.

**How do I update?** In 1.2.1 and later, use **Settings → Update and removal → Check for updates**. For an older version, download the new installer or replace the Mac app once, keeping your existing data folder. Manual downloads remain available for every release.

**Can I change the font?** The app ships with the system font. If you own *TT Norms Pro*, BetterNotes will pick it up — see **Settings → About**.

**Something broke.** Open an [issue](https://github.com/m1koz/betternotes/issues) or write to [t.me/mkships](https://t.me/mkships).

## License

BetterNotes is free to download and use under the [End User License Agreement](LICENSE). © 2026 m1koz. All rights reserved.
