# Algorithms and Pseudocode

This document provides formal step-by-step algorithms and pseudocode for all 10 case studies in the **Python Activity-Based Learning** project. All implementations adhere strictly to introductory first-year programming concepts without external libraries or object-oriented programming.

---

## Case Study 1: Employee Payroll and Deduction Analysis

### Problem Description
Calculate the gross salary and net salary for employees based on basic pay, allowances (HRA, DA), overtime compensation, and incentives. Apply progressive income tax deduction slabs, calculate provident fund (12%), apply fixed statutory deductions, and produce a formatted salary statement.

### Algorithm
1. **Input**: Read `employee_name`, `basic_pay`, `overtime_hours`, and `incentive`.
2. **Calculate Allowances**:
   - `hra = basic_pay * 0.20` (20% House Rent Allowance)
   - `da = basic_pay * 0.10` (10% Dearness Allowance)
   - `overtime_comp = overtime_hours * 500` (Rs. 500/hour)
3. **Calculate Gross Salary**:
   - `gross_salary = basic_pay + hra + da + overtime_comp + incentive`
4. **Determine Progressive Income Tax**:
   - If `gross_salary <= 50,000`: `tax_rate = 0%`, `income_tax = 0`
   - Else if `gross_salary <= 100,000`: `tax_rate = 5%`, `income_tax = gross_salary * 0.05`
   - Else if `gross_salary <= 150,000`: `tax_rate = 10%`, `income_tax = gross_salary * 0.10`
   - Else: `tax_rate = 15%`, `income_tax = gross_salary * 0.15`
5. **Calculate Deductions**:
   - `pf = basic_pay * 0.12` (12% Provident Fund)
   - `other_deductions = 2000.0`
   - `total_deductions = income_tax + pf + other_deductions`
6. **Compute Net Salary**:
   - `net_salary = gross_salary - total_deductions`
7. **Output**: Print formatted tabular salary statement with gross pay, itemized deductions, and net salary.

### Pseudocode
```text
START
    INPUT employee_name, basic_pay, overtime_hours, incentive
    hra = basic_pay * 0.20
    da = basic_pay * 0.10
    overtime_comp = overtime_hours * 500
    gross_salary = basic_pay + hra + da + overtime_comp + incentive

    IF gross_salary <= 50000 THEN
        income_tax = 0.0
    ELSE IF gross_salary <= 100000 THEN
        income_tax = gross_salary * 0.05
    ELSE IF gross_salary <= 150000 THEN
        income_tax = gross_salary * 0.10
    ELSE
        income_tax = gross_salary * 0.15
    END IF

    pf = basic_pay * 0.12
    other_deductions = 2000.0
    total_deductions = income_tax + pf + other_deductions
    net_salary = gross_salary - total_deductions

    PRINT "SALARY STATEMENT"
    PRINT employee_name, basic_pay, hra, da, overtime_comp, incentive
    PRINT gross_salary, income_tax, pf, other_deductions, total_deductions, net_salary
STOP
```

---

## Case Study 2: Retail Billing with Multiple Discount Rules

### Problem Description
Process customer retail purchases with varying quantities, prices, and categories. Apply category-specific sales taxes, evaluate tiered discounts based on invoice subtotal, enforce a maximum discount limit of Rs. 2,000, and generate an itemized invoice.

### Algorithm
1. **Initialize Collections**: Initialize empty lists `products`, `categories`, `quantities`, and `prices`.
2. **Input**: Read `num_products`, then loop `i` from 1 to `num_products` reading `product_name`, `category`, `quantity`, and `unit_price`.
3. **Calculate Subtotal**:
   - `subtotal = sum(quantities[i] * prices[i])` for all items.
4. **Evaluate Discount Rules**:
   - If `subtotal > 10,000`: `discount_percent = 10%`
   - Else if `subtotal > 5,000`: `discount_percent = 5%`
   - Else: `discount_percent = 0%`
   - `discount_amount = subtotal * (discount_percent / 100)`
   - If `discount_amount > 2,000`: `discount_amount = 2,000` (Discount Cap)
   - `taxable_amount = subtotal - discount_amount`
5. **Apply Category Tax**:
   - For each item, category tax is calculated on the pre-discount item gross total (`item_total = quantity * unit_price`):
     - If `category == "Grocery"`: `tax_rate = 0.05` (5%)
     - Else if `category == "Electronics"`: `tax_rate = 0.12` (12%)
     - Else if `category == "Luxury"`: `tax_rate = 0.18` (18%)
     - `item_tax = (quantities[i] * prices[i]) * tax_rate`
     - Accumulate `total_tax += item_tax`
6. **Compute Final Payable**:
   - `final_amount = taxable_amount + total_tax`
   - Policy: Final Payable Amount = (Subtotal - Discount) + Total Tax.
7. **Output**: Print itemized invoice table with item totals, subtotal, discount, total tax, and final payable amount.

### Pseudocode
```text
START
    products = [], categories = [], quantities = [], prices = []
    INPUT num_products
    FOR i = 1 TO num_products DO
        INPUT name, cat, qty, price
        APPEND name TO products, cat TO categories, qty TO quantities, price TO prices
    END FOR

    subtotal = 0.0
    FOR i = 0 TO num_products - 1 DO
        subtotal = subtotal + (quantities[i] * prices[i])
    END FOR

    IF subtotal > 10000 THEN
        discount_percent = 10
    ELSE IF subtotal > 5000 THEN
        discount_percent = 5
    ELSE
        discount_percent = 0
    END IF

    discount_amount = subtotal * (discount_percent / 100)
    IF discount_amount > 2000 THEN
        discount_amount = 2000
    END IF
    taxable_amount = subtotal - discount_amount

    total_tax = 0.0
    FOR i = 0 TO num_products - 1 DO
        item_total = quantities[i] * prices[i]
        IF categories[i] == "Grocery" THEN tax_rate = 0.05
        ELSE IF categories[i] == "Electronics" THEN tax_rate = 0.12
        ELSE tax_rate = 0.18
        item_tax = item_total * tax_rate
        total_tax = total_tax + item_tax
    END FOR

    final_amount = taxable_amount + total_tax
    PRINT Itemized Invoice
STOP
```

---

## Case Study 3: Attendance Recovery Computation

### Problem Description
Calculate a student's current attendance percentage and determine the minimum number of consecutive future classes they must attend to meet or exceed the mandatory 75% attendance threshold.

### Algorithm
1. **Input**: Read `total` classes held and `attended` classes attended.
2. **Compute Current Percentage**:
   - `current_pct = (attended / total) * 100`
3. **Threshold Check**:
   - If `current_pct >= 75.0`:
     - Display attendance is sufficient; no recovery classes required.
   - Else:
     - Initialize `extra = 0`
     - While `((attended + extra) / (total + extra)) * 100 < 75.0`:
       - `extra = extra + 1`
     - Calculate projected new attendance: `new_pct = ((attended + extra) / (total + extra)) * 100`
     - Display required consecutive classes `extra` and projected percentage `new_pct`.
4. **Output**: Print summary report.

### Pseudocode
```text
START
    INPUT total, attended
    current_pct = (attended / total) * 100
    PRINT current_pct

    IF current_pct >= 75.0 THEN
        PRINT "Attendance sufficient (>= 75%). No recovery required."
    ELSE
        extra = 0
        WHILE ((attended + extra) / (total + extra)) * 100 < 75.0 DO
            extra = extra + 1
        END WHILE
        new_pct = ((attended + extra) / (total + extra)) * 100
        PRINT extra, new_pct
    END IF
STOP
```

---

## Case Study 4: Warehouse Inventory Reconciliation

### Problem Description
Reconcile physical warehouse inventory counts against enterprise database records across multiple product lines. Detect stock discrepancies exceeding +/- 5 units and trigger low-stock reorder warnings for items below 20 units.

### Algorithm
1. **Data Initialization**: Initialize parallel lists:
   - `items`: product descriptions
   - `system_qty`: theoretical system stock count
   - `phys_qty`: physical audit count
   - `reorder_level = 20`
2. **Iterate and Reconcile**:
   - For each index `i` from 0 to `len(items) - 1`:
     - `diff = phys_qty[i] - system_qty[i]`
     - Initialize `status = ""`
     - If `abs(diff) > 5`: Append `"DISCREPANCY "`
     - If `phys_qty[i] < reorder_level`: Append `"REORDER"`
     - If `status == ""`: `status = "OK"`
     - Display item row: `item`, `system_qty`, `phys_qty`, `diff`, `status`.
3. **Summary Counts**: Count total discrepancies and reorders.
4. **Output**: Print comprehensive reconciliation table and audit metrics.

### Pseudocode
```text
START
    items = ["Rice Bags", "Sugar", "Oil Cans", "Wheat", "Salt"]
    system_qty = [150, 80, 45, 200, 30]
    phys_qty   = [143, 85, 38, 200, 18]
    reorder_level = 20

    PRINT Header
    FOR i = 0 TO len(items) - 1 DO
        diff = phys_qty[i] - system_qty[i]
        status = ""
        IF abs(diff) > 5 THEN
            status = status + "DISCREPANCY "
        END IF
        IF phys_qty[i] < reorder_level THEN
            status = status + "REORDER"
        END IF
        IF status == "" THEN
            status = "OK"
        END IF
        PRINT items[i], system_qty[i], phys_qty[i], diff, status
    END FOR
STOP
```

---

## Case Study 5: Student Performance Trend Analysis

### Problem Description
Evaluate academic performance for multiple students across multiple courses using a 2D matrix (nested list). Calculate individual student totals and averages, and assign performance classifications (Excellent, Good, Average, Poor).

### Algorithm
1. **Data Initialization**: Define list of `students`, list of `subjects`, and 2D list `marks` (matrix of dimensions students x subjects).
2. **Process Each Student**:
   - For each student row `i`:
     - Initialize `total = 0`
     - For each subject column `j`: `total += marks[i][j]`
     - Compute student average: `avg = total / len(subjects)`
     - Assign grade classification:
       - If `avg >= 80`: `grade = "Excellent"`
       - Else if `avg >= 60`: `grade = "Good"`
       - Else if `avg >= 40`: `grade = "Average"`
       - Else: `grade = "Poor"`
     - Output student row with individual subject scores, average, and grade.
3. **Output**: Print formatted academic performance report.

### Pseudocode
```text
START
    students = ["Ananya", "Bharath", "Chitra"]
    subjects = ["Maths", "Physics", "Chemistry", "Python"]
    marks = [[85, 72, 68, 91], [55, 48, 62, 70], [38, 45, 50, 42]]

    PRINT Header
    FOR i = 0 TO len(students) - 1 DO
        total = 0
        FOR j = 0 TO len(subjects) - 1 DO
            total = total + marks[i][j]
        END FOR
        avg = total / len(subjects)
        IF avg >= 80 THEN grade = "Excellent"
        ELSE IF avg >= 60 THEN grade = "Good"
        ELSE IF avg >= 40 THEN grade = "Average"
        ELSE grade = "Poor"
        PRINT students[i], marks[i], avg, grade
    END FOR
STOP
```

---

## Case Study 6: Student Timetable Conflict Detection

### Problem Description
Inspect a student course enrollment schedule stored as tuples `(course_name, start_hour, end_hour)` in 24-hour format. Detect all pairwise temporal scheduling overlaps preventing simultaneous attendance.

### Algorithm
1. **Data Initialization**: Store course intervals as list of tuples `timetable`.
2. **Pairwise Interval Comparison**:
   - Initialize `conflicts_found = False`
   - For `i` from 0 to `len(timetable) - 1`:
     - Unpack `name_a, start_a, end_a = timetable[i]`
     - For `j` from `i + 1` to `len(timetable) - 1`:
       - Unpack `name_b, start_b, end_b = timetable[j]`
       - **Overlap Condition**:
         - Two open intervals `[start_a, end_a)` and `[start_b, end_b)` overlap if and only if:
           `start_a < end_b and start_b < end_a`
       - If overlap condition is TRUE:
         - Set `conflicts_found = True`
         - Output conflicting course pair and scheduled hours.
3. **Summary**: If `not conflicts_found`, report no conflicts detected.

### Pseudocode
```text
START
    timetable = [("Mathematics", 9, 10), ("Physics", 10, 11), ("Chemistry", 9, 11),
                 ("Python Lab", 14, 16), ("English", 15, 16)]
    conflicts_found = False

    FOR i = 0 TO len(timetable) - 1 DO
        name_a, start_a, end_a = timetable[i]
        FOR j = i + 1 TO len(timetable) - 1 DO
            name_b, start_b, end_b = timetable[j]
            IF start_a < end_b AND start_b < end_a THEN
                PRINT "CONFLICT:", name_a, "overlaps with", name_b
                conflicts_found = True
            END IF
        END FOR
    END FOR

    IF NOT conflicts_found THEN
        PRINT "No conflicts detected."
    END IF
STOP
```

---

## Case Study 7: Repeated Transaction Detection

### Problem Description
Identify potential double billing or fraudulent duplicate transactions within a banking transaction ledger. Flag and deduplicate all transaction pairs where the transaction amount and merchant name match identically.

### Algorithm
1. **Data Initialization**: Define list of transaction tuples `(transaction_id, amount, merchant)`.
2. **Pairwise Ledger Scan**:
   - Initialize empty list `flagged = []`
   - For `i` from 0 to `len(transactions) - 1`:
     - Unpack `tid_a, amt_a, mer_a = transactions[i]`
     - For `j` from `i + 1` to `len(transactions) - 1`:
       - Unpack `tid_b, amt_b, mer_b = transactions[j]`
       - If `amt_a == amt_b and mer_a == mer_b`:
         - Create record `pair = (tid_a, tid_b, amt_a, mer_a)`
         - If `pair not in flagged`: Append `pair` to `flagged`.
3. **Output**:
   - If `flagged` is non-empty: Print table of duplicate transactions with warning flags.
   - Else: Print "No repeated transactions found."
   - Display total count of flagged duplicate pairs.

### Pseudocode
```text
START
    transactions = [("T001", 500.0, "Amazon"), ("T002", 1200.0, "Flipkart"),
                    ("T003", 500.0, "Amazon"), ("T004", 750.0, "Swiggy"),
                    ("T005", 1200.0, "Flipkart"), ("T006", 300.0, "Zomato"),
                    ("T007", 500.0, "Amazon")]
    flagged = []

    FOR i = 0 TO len(transactions) - 1 DO
        tid_a, amt_a, mer_a = transactions[i]
        FOR j = i + 1 TO len(transactions) - 1 DO
            tid_b, amt_b, mer_b = transactions[j]
            IF amt_a == amt_b AND mer_a == mer_b THEN
                pair = (tid_a, tid_b, amt_a, mer_a)
                IF pair NOT IN flagged THEN
                    APPEND pair TO flagged
                END IF
            END IF
        END FOR
    END FOR

    IF len(flagged) > 0 THEN
        PRINT flagged transactions
    ELSE
        PRINT "No repeated transactions found."
    END IF
STOP
```

---

## Case Study 8: Nested Loop Calendar Generator

### Problem Description
Generate a 7-column monthly calendar (Monday through Sunday) for any given Gregorian month and year. Compute leap years, days per month, and starting day offset without using the standard `calendar` module.

### Algorithm
1. **Input**: Read `month` (1-12) and `year`.
2. **Leap Year Determination**:
   - Function `is_leap(year)`: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`
3. **Determine Month Days**:
   - Days array: `[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`
   - If `month == 2` and `is_leap(year)`: `total_days = 29`, else `days[month]`.
4. **Determine Starting Weekday (Tomohiko Sakamoto's Algorithm)**:
   - Adjustment table: `t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]`
   - If `month < 3`: `y = year - 1`, else `y = year`.
   - `d = (y + y//4 - y//100 + y//400 + t[month-1] + 1) % 7` (0 = Sunday .. 6 = Saturday)
   - Convert to Monday = 0: `start = (d + 6) % 7`
5. **Generate Calendar Grid with Nested Loops**:
   - Print headers: `Mon  Tue  Wed  Thu  Fri  Sat  Sun`
   - Initialize `day = 1`
   - Outer loop `week` from 0 to 5 (weeks):
     - Inner loop `col` from 0 to 6 (days of week):
       - `cell = week * 7 + col`
       - If `cell < start` or `day > total_days`:
         - Print 5 empty spaces
       - Else:
         - Print formatted `day` right-aligned with 4 width + 1 space
         - `day = day + 1`
     - Print newline
     - If `day > total_days`: Break outer loop.
6. **Output**: Formatted calendar grid.

### Pseudocode
```text
START
    INPUT month, year
    total_days = days_in_month(month, year)
    start = start_day(month, year)

    PRINT month_name, year
    PRINT "Mon  Tue  Wed  Thu  Fri  Sat  Sun"
    day = 1
    FOR week = 0 TO 5 DO
        FOR col = 0 TO 6 DO
            cell = week * 7 + col
            IF cell < start OR day > total_days THEN
                PRINT "     "
            ELSE
                PRINT formatted day
                day = day + 1
            END IF
        END FOR
        PRINT newline
        IF day > total_days THEN BREAK
    END FOR
STOP
```

---

## Case Study 9: Student Marks Matrix Analysis

### Problem Description
Represent student academic records as a 2D matrix (nested list). Perform statistical matrix operations including individual student row totals and averages, subject-wise column averages, global highest and lowest marks, and identify the top student and best subject.

### Algorithm
1. **Data Initialization**: Define list of `students`, `subjects`, and 2D matrix `marks`.
2. **Compute Row Totals and Averages**:
   - Initialize `row_totals = []`
   - For each student `i`:
     - `total = sum(marks[i])`
     - `avg = total / len(subjects)`
     - Append `total` to `row_totals`
     - Print student row: name, individual marks, total, average.
3. **Compute Column Averages (Subject-wise)**:
   - Initialize `col_avgs = []`
   - For each subject `j`:
     - `col_sum = sum(marks[i][j] for i in range(len(students)))`
     - `col_avg = col_sum / len(students)`
     - Append `col_avg` to `col_avgs`
     - Print `col_avg` formatted under each subject column.
4. **Identify Matrix Extremes**:
   - Flatten matrix: `all_marks = [marks[i][j] for all i, j]`
   - `highest_mark = max(all_marks)`
   - `lowest_mark = min(all_marks)`
   - Top student: `students[row_totals.index(max(row_totals))]`
   - Best subject: `subjects[col_avgs.index(max(col_avgs))]`
5. **Output**: Print comprehensive matrix table and summary analytics.

### Pseudocode
```text
START
    students = ["Arun", "Bala", "Divya", "Esha"]
    subjects = ["Maths", "Science", "English", "Python"]
    marks = [[88, 76, 65, 92], [55, 60, 72, 48],
             [91, 85, 88, 95], [70, 55, 60, 75]]

    PRINT Table Header
    row_totals = []
    FOR i = 0 TO len(students) - 1 DO
        total = SUM(marks[i])
        avg = total / len(subjects)
        APPEND total TO row_totals
        PRINT students[i], marks[i], total, avg
    END FOR

    col_avgs = []
    FOR j = 0 TO len(subjects) - 1 DO
        col_sum = SUM(marks[i][j] for i from 0 to len(students)-1)
        col_avg = col_sum / len(students)
        APPEND col_avg TO col_avgs
    END FOR
    PRINT "Col Avg", col_avgs

    highest = MAX(all_marks), lowest = MIN(all_marks)
    top_student = students[INDEX_OF_MAX(row_totals)]
    best_subject = subjects[INDEX_OF_MAX(col_avgs)]
    PRINT highest, lowest, top_student, best_subject
STOP
```

---

## Case Study 10: Smart Canteen Order and Stock Management

### Problem Description
Manage a campus food canteen order processing system. Maintain real-time inventory counts in a mutable menu table, validate item stock before fulfillment, compute customer billing with bulk purchase discounts (10% if subtotal > Rs. 200), and perform end-of-day low-stock inventory audits (< 5 units).

### Algorithm
1. **Initialize Menu**: List of mutable items: `[item_name, price, stock_qty]`.
2. **Display Menu**: Enumerate and print current menu with prices and stock levels.
3. **Process Order**:
   - Input `num_items` to order.
   - For each item ordered:
     - Input `choice` (1-based index) and `qty`.
     - Convert `choice = choice - 1`.
     - Check stock:
       - If `menu[choice][2] >= qty`:
         - Deduct inventory: `menu[choice][2] -= qty`
         - Accumulate billing: `bill_total += menu[choice][1] * qty`
         - Record ordered item name and quantity.
       - Else: Display "Insufficient stock" message.
4. **Compute Discounts**:
   - If `bill_total > 200`: `discount = bill_total * 0.10`
   - Else: `discount = 0.0`
   - `payable = bill_total - discount`
5. **Print Order Invoice**:
   - Itemized list of purchased items, subtotal, discount, and payable amount.
6. **Low Stock Audit**:
   - Iterate through `menu`:
     - If `stock < 5`: Trigger alert flag and print warning.
   - If no items below 5: Print "All canteen items are adequately stocked."

### Pseudocode
```text
START
    menu = [["Idli", 20, 50], ["Dosa", 30, 40], ["Sambar", 10, 80],
            ["Tea", 8, 100], ["Coffee", 12, 60], ["Rice Meal", 60, 20]]
    PRINT Menu

    order_items = [], order_qty = [], bill_total = 0.0
    INPUT num_items
    FOR k = 1 TO num_items DO
        INPUT choice, qty
        choice = choice - 1
        IF menu[choice][2] >= qty THEN
            menu[choice][2] = menu[choice][2] - qty
            bill_total = bill_total + (menu[choice][1] * qty)
            APPEND menu[choice][0] TO order_items, qty TO order_qty
        ELSE
            PRINT "Insufficient stock!"
        END IF
    END FOR

    IF bill_total > 200 THEN
        discount = bill_total * 0.10
    ELSE
        discount = 0.0
    END IF
    payable = bill_total - discount

    PRINT Order Bill, subtotal, discount, payable

    PRINT "LOW STOCK ALERT REPORT"
    alert = False
    FOR item IN menu DO
        IF item[2] < 5 THEN
            PRINT "ALERT: Low stock on", item[0]
            alert = True
        END IF
    END FOR
    IF NOT alert THEN PRINT "All items adequately stocked."
STOP
```
