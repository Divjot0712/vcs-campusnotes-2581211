"""
CampusNotes - Search and Filter Module
Contributed by Partner: Nilay Nayyar (2581066)
Branch: feature/nilay-notes-search
"""

import os
from typing import List

def search_notes(query: str, notes_dir: str = "notes") -> List[str]:
    """Search for keywords across all campus notes files with case-insensitivity."""
    if not os.path.exists(notes_dir):
        return []
    
    matching_notes: List[str] = []
    for filename in sorted(os.listdir(notes_dir)):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(notes_dir, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Perform case-insensitive search to improve note retrieval
                    if query.lower() in content.lower():
                        matching_notes.append(filename)
            except (IOError, UnicodeDecodeError):
                continue
    return matching_notes

def filter_by_subject(subject_code: str, notes_dir: str = "notes") -> List[str]:
    """Filter notes belonging to a specific course subject."""
    if not os.path.exists(notes_dir):
        return []
    return [
        f for f in sorted(os.listdir(notes_dir))
        if subject_code.lower() in f.lower()
    ]
