# Changelog

All notable changes to BetterNotes are documented here.

## [1.2.1] — 2026-10-05

### Fixed
- Highlight and text colour no longer continue onto the next word when typing at the end of a coloured passage
- Pending saves finish before updating or removing the application

### Added
- Remove colour in the editor toolbar and colour picker; clears text colour and highlighting while keeping other formatting
- In-app update checks, verified signed downloads, progress and restart after installation
- A safety copy of the application and data before installation or removal
- Remove app in Settings; notes, projects, attachments and backups stay in place
- Translated maintenance controls, confirmations, progress and errors in all ten languages

### Distribution
- Universal macOS app (Apple silicon and Intel), Windows x64 installer and portable app
- Signed update packages and an update manifest for both platforms
- Versions older than 1.2.1 require one manual update to enable in-app updates

## [1.2.0] — 2026-10-05

### Added
- Project branches: topics with their own tasks, notes, folders, files and links, including optional nested branches
- Independent branch settings to include tasks in project progress
- Text highlighting with colour presets, a custom colour picker and HEX input; optional text colour formatting in notes and task notes
- Search, full exports and backups include branch content and attachments

### Improved
- The Branches tab is placed immediately after Overview
- Project duplication, calendar task navigation and attachment cleanup support nested branches
- New controls are translated into all ten interface languages
- Universal macOS build for Apple silicon and Intel, plus Windows installer and portable build

## [1.1.0] — 2026-09-15

First public release for macOS and Windows.

### Added
- Notes with rich text, checklists, tags, comments, pinning and pictures that resize with the mouse
- Projects with tasks and deadlines; notes, links and files inside a task; a file explorer with folders and drag-and-drop; photos, links and a discussion thread per project
- Plans by day, week, month and year with progress that rolls up from the bottom, date ranges, a daily log and one-click reports
- Week calendar by hours: events with description and color, drag to move, pull to resize; task deadlines and goals in the all-day strip
- Home with the day's events, upcoming goals, pinned and recent items
- Search across everything, including the contents of attached text files (⌘K / Ctrl+K)
- Statistics
- Dark and light themes that can follow the system
- Ten interface languages; the system language is picked on first launch
- Data as plain files in a `data/` folder next to the app, with export, import and automatic daily and weekly backups
- Native app for macOS 11+ (Apple silicon and Intel) and Windows 10/11, installer and portable builds
