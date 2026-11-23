"""
Case Study 9: Student Marks Matrix Analysis
Concepts Used: 2D Nested Lists, Row & Column Traversals, Aggregation (sum, min, max, average).
"""

def main():
    print("=" * 55)
    print("              MARKS MATRIX ANALYSIS")
    print("=" * 55)

    students = ["Arun", "Bala", "Divya", "Esha"]
    subjects = ["Maths", "Science", "English", "Python"]
    marks = [
        [88, 76, 65, 92],  # Arun
        [55, 60, 72, 48],  # Bala
        [91, 85, 88, 95],  # Divya
        [70, 55, 60, 75]   # Esha
    ]

    # Header
    print(f"{'Student':<10}", end="")
    for s in subjects:
        print(f"{s:>10}", end="")
    print(f"{'Total':>8}{'Avg':>7}")
    print("-" * 55)

    # Student-wise (Row) Totals and Averages
    row_totals = []
    for i in range(len(students)):
        total = sum(marks[i])
        avg = total / len(subjects)
        row_totals.append(total)
        print(f"{students[i]:<10}", end="")
        for m in marks[i]:
            print(f"{m:>10}", end="")
        print(f"{total:>8}{avg:>7.1f}")

    print("-" * 55)

    # Subject-wise (Column) Averages
    print(f"{'Col Avg':<10}", end="")
    col_avgs = []
    for j in range(len(subjects)):
        col_sum = sum(marks[i][j] for i in range(len(students)))
        col_avg = col_sum / len(students)
        col_avgs.append(col_avg)
        print(f"{col_avg:>10.1f}", end="")
    print()
    print("=" * 55)

    # Global Matrix Statistics
    all_marks = [marks[i][j] for i in range(len(students)) for j in range(len(subjects))]
    highest_mark = max(all_marks)
    lowest_mark = min(all_marks)

    top_idx = row_totals.index(max(row_totals))
    best_sub = col_avgs.index(max(col_avgs))

    print(f"Highest Mark in Class : {highest_mark}")
    print(f"Lowest Mark in Class  : {lowest_mark}")
    print(f"Top Performing Student: {students[top_idx]} (Total: {max(row_totals)})")
    print(f"Best Subject Average  : {subjects[best_sub]} (Avg: {max(col_avgs):.1f})")
    print("=" * 55)

if __name__ == "__main__":
    main()
