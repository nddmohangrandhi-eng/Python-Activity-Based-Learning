"""
Case Study 6: Student Timetable Conflict Detection
Concepts Used: Tuples, Tuple Unpacking, Nested Loops, Overlap Comparison Logic.
"""

def main():
    print("=" * 55)
    print("           TIMETABLE CONFLICT DETECTION REPORT")
    print("=" * 55)

    # Tuples store: (course_name, start_hour, end_hour) in 24-hour format
    timetable = [
        ("Mathematics",  9, 10),
        ("Physics",      10, 11),
        ("Chemistry",    9, 11),
        ("Python Lab",   14, 16),
        ("English",      15, 16)
    ]

    conflicts_found = False
    conflict_count = 0

    print(f"{'Course A':<15}{'Slot A':<12}{'Course B':<15}{'Slot B':<12}")
    print("-" * 55)

    # Pairwise comparison to detect overlapping intervals
    for i in range(len(timetable)):
        name_a, start_a, end_a = timetable[i]
        for j in range(i + 1, len(timetable)):
            name_b, start_b, end_b = timetable[j]

            # Overlap condition: start_a < end_b and start_b < end_a
            if start_a < end_b and start_b < end_a:
                conflicts_found = True
                conflict_count += 1
                slot_a = f"{start_a:02d}:00-{end_a:02d}:00"
                slot_b = f"{start_b:02d}:00-{end_b:02d}:00"
                print(f"{name_a:<15}{slot_a:<12}{name_b:<15}{slot_b:<12}")

    print("-" * 55)
    if not conflicts_found:
        print("No timetable conflicts detected. All courses scheduled smoothly.")
    else:
        print(f"Total Overlapping Conflicts Detected: {conflict_count}")
    print("=" * 55)

if __name__ == "__main__":
    main()
