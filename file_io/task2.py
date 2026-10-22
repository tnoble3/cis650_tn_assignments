import json
from datetime import date
from pathlib import Path

JSON_FILE = Path(__file__).resolve().parent / "study_log.json"

def load_sessions():
    with JSON_FILE.open("r", encoding="utf-8") as file:
        sessions = json.load(file)
    if not isinstance(sessions, list):
        raise ValueError("The JSON file must contain an array of study sessions.")
    for session in sessions:
        if not isinstance(session, dict) or not all(
            field in session for field in ("date", "course", "minutes", "note")
        ):
            raise ValueError("Each session must have date, course, minutes, and note.")
    return sessions

def course_names(sessions):
    return sorted({session["course"] for session in sessions}, key=str.casefold)

def total_time_per_course(sessions):
    totals = {}
    for session in sessions:
        course = session["course"]
        totals[course] = totals.get(course, 0) + int(session["minutes"])
    return totals

def most_active_course(sessions):
    counts = {}
    for session in sessions:
        course = session["course"]
        counts[course] = counts.get(course, 0) + 1
    if not counts:
        return None, 0
    return max(counts.items(), key=lambda item: item[1])

def average_session_length(sessions, course):
    minutes = [int(item["minutes"]) for item in sessions if item["course"] == course]
    if not minutes:
        return None
    return round(sum(minutes) / len(minutes), 1)

def course_dates_and_notes(sessions, course):
    results = [
        (item["date"], item["note"])
        for item in sessions
        if item["course"] == course
    ]
    return sorted(results, key=lambda item: date.fromisoformat(item[0]))


def ask_for_course(sessions):
    courses = course_names(sessions)
    print("Available courses: " + ", ".join(courses))
    while True:
        answer = input("Enter course name: ").strip()
        match = next((name for name in courses if name.casefold() == answer.casefold()), None)
        if match is not None:
            return match
        print("Invalid course. Choose one of the available courses.")

def main():
    try:
        sessions = load_sessions()
    except (FileNotFoundError, json.JSONDecodeError, ValueError, OSError) as error:
        print(f"Cannot load {JSON_FILE.name}: {error}")
        return
    if not sessions:
        print("No study sessions found.")
        return

    while True:
        print("\n===== Study Session Menu =====")
        print("1. Total study time per course")
        print("2. Most active course")
        print("3. Average session length")
        print("4. View course dates and notes")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nTotal study time by course:")
            for course, total in sorted(total_time_per_course(sessions).items()):
                hours, minutes = divmod(total, 60)
                print(f"{course}: {hours} hour(s) and {minutes} minute(s)")
        elif choice == "2":
            course, count = most_active_course(sessions)
            print(f"Most active course: {course} ({count} sessions)")
        elif choice == "3":
            course = ask_for_course(sessions)
            average = average_session_length(sessions, course)
            print(f"Average session length for {course}: {average:.1f} minutes")
        elif choice == "4":
            course = ask_for_course(sessions)
            print(f"\nDates and notes for {course}:")
            for session_date, note in course_dates_and_notes(sessions, course):
                print(f"{session_date} | {note}")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid menu option. Enter a number from 1 to 5.")

if __name__ == "__main__":
    main()