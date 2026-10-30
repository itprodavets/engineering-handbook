# Data storage and SQLite

[Русский](storage.md) · [English](storage.en.md)

[Home](../README.en.md) · [Layout](repository-layout.en.md)

**No SQLite backend is needed yet.** Git and `content/*.json` provide versioning, stable IDs, and canonical knowledge. Markdown under `topics/` and `questions/` is generated; executable source lives under `labs/`.

GitHub Pages is static hosting. A SQLite file checked into the site does not provide secure, authenticated writes for learners. Browser progress uses device-local `localStorage`; personal scores and answers remain in a separate private Google Sheet.

**Revisit a database** when cross-device synchronization, account login, attempts history, or analytics require an authenticated backend. SQLite may suit a small single-instance app; PostgreSQL could suit a larger multi-user service. SQLite itself can still be studied as a database topic with labs.
