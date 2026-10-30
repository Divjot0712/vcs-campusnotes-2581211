"""
CampusNotes - Search and Filter Module
Contributed by Partner: Nilay Nayyar (2581066)
Branch: feature/nilay-notes-search
"""

import os

def search_notes(query, notes_dir="notes"):
    """Search for keywords across all campus notes files."""
    if not os.path.exists(notes_dir):
        return []
    
    matching_notes = []
    for filename in sorted(os.listdir(notes_dir)):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(notes_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                # Basic substring check
                if query in content:
                    matching_notes.append(filename)
    return matching_notes

def filter_by_subject(subject_code, notes_dir="notes"):
    """Filter notes belonging to a specific course subject."""
    return [
        f for f in sorted(os.listdir(notes_dir))
        if subject_code.lower() in f.lower()
    ]
