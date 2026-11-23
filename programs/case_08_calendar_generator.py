"""
Case Study 8: Nested Loop Calendar Generator
Concepts Used: Functions, Nested Loops (Weeks x Days), Offsets, Modular Arithmetic, Formatting.
"""
import sys

def get_input(prompt=""):
    val = input(prompt)
    if not sys.stdin.isatty():
        print(val)
    return val

def is_leap(year):
    """Check if a year is a leap year according to Gregorian calendar rules."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return number of days in the specified month and year."""
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return days[month]

def start_day(month, year):
    """
    Calculate starting day of week using Tomohiko Sakamoto's algorithm.
    Returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday.
    """
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y = year
    if month < 3:
        y -= 1
    # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    d = (y + y // 4 - y // 100 + y // 400 + t[month - 1] + 1) % 7
    # Convert so Monday is 0 and Sunday is 6
    return (d + 6) % 7

def main():
    print("=" * 35)
    print("     MONTHLY CALENDAR GENERATOR")
    print("=" * 35)

    month = int(get_input("Enter month (1-12): "))
    year = int(get_input("Enter year: "))

    months = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    total_days = days_in_month(month, year)
    start = start_day(month, year)

    print("\n" + "=" * 35)
    print(f"          {months[month]} {year}")
    print("=" * 35)
    print(" Mon  Tue  Wed  Thu  Fri  Sat  Sun")
    print("-" * 35)

    day = 1
    # Up to 6 weeks in a month calendar grid
    for week in range(6):
        for col in range(7):
            cell = week * 7 + col
            if cell < start or day > total_days:
                print("     ", end="")
            else:
                print(f"{day:>4} ", end="")
                day += 1
        print()
        if day > total_days:
            break
    print("=" * 35)

if __name__ == "__main__":
    main()
