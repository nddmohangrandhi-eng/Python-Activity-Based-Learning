"""
Case Study 3: Attendance Recovery Computation
Concepts Used: While Loop, Conditionals (if-else), Arithmetic Operators, Percentage Calculation.
"""
import sys

def get_input(prompt=""):
    val = input(prompt)
    if not sys.stdin.isatty():
        print(val)
    return val

def main():
    print("=" * 55)
    print("       ATTENDANCE RECOVERY COMPUTATION SYSTEM")
    print("=" * 55)

    total = int(get_input("Total classes held: "))
    attended = int(get_input("Classes attended: "))

    current_pct = (attended / total) * 100
    print(f"\nCurrent Attendance: {current_pct:.2f}%")

    if current_pct >= 75.0:
        print("Attendance is sufficient (>= 75.00%). No recovery needed.")
    else:
        extra = 0
        # Calculate minimum additional consecutive classes needed to achieve >= 75%
        while ((attended + extra) / (total + extra)) * 100 < 75.0:
            extra += 1

        new_pct = ((attended + extra) / (total + extra)) * 100
        print(f"Target Threshold           : 75.00%")
        print(f"Consecutive Classes Needed : {extra}")
        print(f"Projected Total Classes    : {total + extra}")
        print(f"Projected Attended Classes : {attended + extra}")
        print(f"Attendance after attending : {new_pct:.2f}%")

    print("=" * 55)

if __name__ == "__main__":
    main()
