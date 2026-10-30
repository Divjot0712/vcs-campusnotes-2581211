# CampusNotes

CampusNotes is a collaborative academic note-sharing and revision management system developed for VCS Assignment 2.

## Student Information
- **Name:** Divjot Singh
- **Enrollment Number:** 2581211
- **Course:** Version Control Systems (CSE25303)
- **Repository:** vcs-campusnotes-2581211

## Architecture & Features
- Modular notes management (`notes/notes_manager.py`)
- Lecture summary indexing and revision notes
- Tagging and search filtering
- Markdown export utilities for coursework submission

## Module Guide
- `notes/notes_manager.py`: Core utility class `CampusNotes` for note listing, reading, and tag filtering.
- `modules/search_filter.py`: Keyword searching across lecture summaries and subject filtering.

## Running Tests
Run unit execution:
```bash
python3 notes/notes_manager.py
python3 -c "from modules.search_filter import search_notes; print(search_notes('git'))"
```
