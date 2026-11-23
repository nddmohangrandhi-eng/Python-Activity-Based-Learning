"""
Case Study 1: Employee Payroll and Deduction Analysis
Concepts Used: Variables, Data Types (int, float), Arithmetic Operators,
               Conditional Statements (if-elif-else), String Formatting.
"""
import sys

def get_input(prompt=""):
    val = input(prompt)
    if not sys.stdin.isatty():
        print(val)
    return val

def main():
    print("=" * 50)
    print("     EMPLOYEE PAYROLL & DEDUCTION ANALYSIS")
    print("=" * 50)
    
    # Input employee details
    employee_name = get_input("Enter employee name: ")
    basic_pay = float(get_input("Enter basic pay: "))
    overtime_hours = float(get_input("Enter overtime hours: "))
    incentive = float(get_input("Enter incentive amount: "))

    # Calculate allowances and overtime compensation
    # HRA: 20% of basic pay, DA: 10% of basic pay, Overtime rate: Rs. 500/hr
    hra = basic_pay * 0.20
    da = basic_pay * 0.10
    overtime_comp = overtime_hours * 500

    # Calculate Gross Salary
    gross_salary = basic_pay + hra + da + overtime_comp + incentive

    # Progressive Income Tax Slabs:
    # Up to Rs. 50,000       : 0%
    # Rs. 50,001 - 1,00,000  : 5%
    # Rs. 1,00,001 - 1,50,000: 10%
    # Above Rs. 1,50,000     : 15%
    if gross_salary <= 50000:
        tax_rate_pct = 0
        income_tax = 0.0
    elif gross_salary <= 100000:
        tax_rate_pct = 5
        income_tax = gross_salary * 0.05
    elif gross_salary <= 150000:
        tax_rate_pct = 10
        income_tax = gross_salary * 0.10
    else:
        tax_rate_pct = 15
        income_tax = gross_salary * 0.15

    # Statutory Deductions
    # Provident Fund: 12% of basic pay, Fixed other deductions: Rs. 2,000
    pf = basic_pay * 0.12
    other_deductions = 2000.0
    total_deductions = income_tax + pf + other_deductions

    # Compute Net Salary
    net_salary = gross_salary - total_deductions

    # Display Formatted Salary Statement
    print("\n" + "=" * 50)
    print("           SALARY STATEMENT")
    print("=" * 50)
    print(f"Employee Name         : {employee_name}")
    print(f"Basic Pay             : Rs.{basic_pay:,.2f}")
    print(f"HRA (20%)             : Rs.{hra:,.2f}")
    print(f"DA  (10%)             : Rs.{da:,.2f}")
    print(f"Overtime Compensation : Rs.{overtime_comp:,.2f}")
    print(f"Incentive             : Rs.{incentive:,.2f}")
    print("-" * 50)
    print(f"GROSS SALARY          : Rs.{gross_salary:,.2f}")
    print("-" * 50)
    print(f"Income Tax ({tax_rate_pct}%)       : Rs.{income_tax:,.2f}")
    print(f"Provident Fund (12%)  : Rs.{pf:,.2f}")
    print(f"Other Deductions      : Rs.{other_deductions:,.2f}")
    print("-" * 50)
    print(f"Total Deductions      : Rs.{total_deductions:,.2f}")
    print("=" * 50)
    print(f"NET SALARY            : Rs.{net_salary:,.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()
