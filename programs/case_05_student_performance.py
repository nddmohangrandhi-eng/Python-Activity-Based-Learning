"""
Case Study 5: Student Performance Trend Analysis
Concepts Used: Nested Lists (2D Arrays), Nested Loops, Conditionals, Arithmetic Averaging.
"""

def main():
    print("=" * 62)
    print("        STUDENT PERFORMANCE TREND ANALYSIS REPORT")
    print("=" * 62)

    students = ["Ananya", "Bharath", "Chitra"]
    subjects = ["Maths", "Physics", "Chemistry", "Python"]
    marks = [
        [85, 72, 68, 91],  # Ananya
        [55, 48, 62, 70],  # Bharath
        [38, 45, 50, 42]   # Chitra
    ]

    # Print Table Header
    print(f"{'Student':<10}", end="")
    for sub in subjects:
        print(f"{sub:>10}", end="")
    print(f"{'Avg':>8}  {'Grade':<10}")
    print("-" * 62)

    # Process each student
    for i in range(len(students)):
        total = 0
        for j in range(len(subjects)):
            total += marks[i][j]
        avg = total / len(subjects)

        # Performance Classification:
        # >= 80: Excellent, >= 60: Good, >= 40: Average, < 40: Poor
        if avg >= 80:
            grade = "Excellent"
        elif avg >= 60:
            grade = "Good"
        elif avg >= 40:
            grade = "Average"
        else:
            grade = "Poor"

        print(f"{students[i]:<10}", end="")
        for m in marks[i]:
            print(f"{m:>10}", end="")
        print(f"{avg:>8.1f}  {grade:<10}")

    print("=" * 62)

if __name__ == "__main__":
    main()
