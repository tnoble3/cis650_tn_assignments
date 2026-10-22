import json
from datetime import date
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
TEXT_FILE = BASE_DIR / "study_log.txt"
JSON_FILE = BASE_DIR / "study_log.json"

def validate_course():
    while True:
        course = input("Enter course: ").strip()
        if course:
            return course
        print("Course cannot be empty. Please try again.")

def validate_minutes():
    while True:
        value = input("Enter minutes studied: ").strip()
        try:
            minutes = int(value)
            if minutes > 0:
                return minutes
        except ValueError:
            pass
        print("Minutes must be a positive whole number.")

def validate_note():
    while True:
        note = input("Enter a one-line note: ").strip()
        if note and "\n" not in note and "\r" not in note:
            return note
        print("Note cannot be empty. Please try again.")

def save_text_entry(entry):
    line = f"{entry['date']} | {entry['course']} | {entry['minutes']} | {entry['note']}\n"
    with TEXT_FILE.open("a", encoding="utf-8") as file:
        file.write(line)

def save_json_entry(entry):
    entries = []
    if JSON_FILE.exists():
        try:
            with JSON_FILE.open("r", encoding="utf-8") as file:
                entries = json.load(file)
        except (json.JSONDecodeError, OSError) as error:
            raise ValueError("Cannot read existing study_log.json; no changes were made to it.") from error
        if not isinstance(entries, list):
            raise ValueError("study_log.json must contain a JSON array.")
    entries.append(entry)
    with JSON_FILE.open("w", encoding="utf-8") as file:
        json.dump(entries, file, indent=4)
        file.write("\n")

def display_history():
    for title, path in (("Text History", TEXT_FILE), ("JSON History", JSON_FILE)):
        print(f"\n--- {title} ---")
        with path.open("r", encoding="utf-8") as file:
            print(file.read(), end="\n")

def main():
    entry = {
        "date": date.today().isoformat(),
        "course": validate_course(),
        "minutes": validate_minutes(),
        "note": validate_note(),
    }
    # validate the existing JSON before modifying either file.
    if JSON_FILE.exists():
        try:
            with JSON_FILE.open("r", encoding="utf-8") as file:
                existing = json.load(file)
            if not isinstance(existing, list):
                raise ValueError("study_log.json must contain a JSON array.")
        except json.JSONDecodeError as error:
            print(f"Invalid JSON file: {error}")
            return
    save_text_entry(entry)
    save_json_entry(entry)
    print("\nSession saved successfully!")
    display_history()

if __name__ == "__main__":
    main()