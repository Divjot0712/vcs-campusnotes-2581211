"""
CampusNotes - Student Academic Notes Management Utility
Author: Divjot Singh (Enrollment: 2581211)
Course: Version Control Systems (CSE25303)
"""

import os

class CampusNotes:
    def __init__(self, storage_dir="notes"):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir, exist_ok=True)

    def list_notes(self):
        """List all text and markdown notes in the storage folder."""
        return sorted([
            f for f in os.listdir(self.storage_dir)
            if f.endswith(".txt") or f.endswith(".md")
        ])

    def read_note(self, filename):
        """Read the content of a specific note file."""
        filepath = os.path.join(self.storage_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Note '{filename}' does not exist.")
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def add_note(self, filename, content):
        """Add or update an academic note file."""
        filepath = os.path.join(self.storage_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

if __name__ == "__main__":
    app = CampusNotes()
    print("CampusNotes System Initialized.")
    print("Available Notes:", app.list_notes())

    def get_notes_by_tag(self, tag):
        """Filter notes containing a specific hashtag/tag keyword."""
        results = []
        for name in self.list_notes():
            try:
                content = self.read_note(name)
                if tag.lower() in content.lower():
                    results.append(name)
            except Exception:
                continue
        return results

    def safe_read(self, filename):
        """Safely read note content with graceful error fallback."""
        try:
            return self.read_note(filename)
        except FileNotFoundError:
            return "[Error: Note file not found]"
        except UnicodeDecodeError:
            return "[Error: File decoding failed]"

    def get_storage_path(self, filename=None):
        """Unified path resolver for storage directory and files."""
        base = os.path.abspath(self.storage_dir)
        return os.path.join(base, filename) if filename else base
