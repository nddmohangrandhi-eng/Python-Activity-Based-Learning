# Program Flowcharts

This document provides visual flowcharts for all 10 case studies in the **Python Activity-Based Learning** project using GitHub-compatible Mermaid diagrams.

---

## Case Study 1: Employee Payroll and Deduction Analysis

```mermaid
flowchart TD
    Start([Start]) --> Input[/"Input employee_name, basic_pay, overtime_hours, incentive"/]
    Input --> Allowances["Calculate Allowances:<br>HRA = 20% of basic<br>DA = 10% of basic<br>Overtime = hours * 500"]
    Allowances --> Gross["gross_salary = basic + HRA + DA + Overtime + incentive"]
    Gross --> Cond1{"gross_salary <= 50,000?"}
    Cond1 -- Yes --> Tax0["tax_rate = 0%<br>income_tax = 0"]
    Cond1 -- No --> Cond2{"gross_salary <= 100,000?"}
    Cond2 -- Yes --> Tax5["tax_rate = 5%<br>income_tax = gross * 0.05"]
    Cond2 -- No --> Cond3{"gross_salary <= 150,000?"}
    Cond3 -- Yes --> Tax10["tax_rate = 10%<br>income_tax = gross * 0.10"]
    Cond3 -- No --> Tax15["tax_rate = 15%<br>income_tax = gross * 0.15"]
    Tax0 --> SlabsDone[Merge Tax Result]
    Tax5 --> SlabsDone
    Tax10 --> SlabsDone
    Tax15 --> SlabsDone
    SlabsDone --> Deductions["PF = basic * 0.12<br>other_deductions = 2000<br>total_deductions = income_tax + PF + other_deductions"]
    Deductions --> Net["net_salary = gross_salary - total_deductions"]
    Net --> Display[/"Display Formatted Salary Statement"/]
    Display --> End([End])
```

---

## Case Study 2: Retail Billing with Multiple Discount Rules

```mermaid
flowchart TD
    Start([Start]) --> Init["Initialize lists: products, categories, quantities, prices"]
    Init --> InputN[/"Input num_products"/]
    InputN --> LoopInput{"More products to input?"}
    LoopInput -- Yes --> ReadItem[/"Input name, category, quantity, unit_price"/]
    ReadItem --> AppendItem["Append values to respective lists"]
    AppendItem --> LoopInput
    LoopInput -- No --> CalcSubtotal["subtotal = sum(quantities[i] * prices[i])"]
    CalcSubtotal --> DiscCheck{"subtotal > 10,000?"}
    DiscCheck -- Yes --> Disc10["discount_percent = 10%"]
    DiscCheck -- No --> DiscCheck5{"subtotal > 5,000?"}
    DiscCheck5 -- Yes --> Disc5["discount_percent = 5%"]
    DiscCheck5 -- No --> Disc0["discount_percent = 0%"]
    Disc10 --> CalcDisc["discount_amount = subtotal * (discount_percent / 100)"]
    Disc5 --> CalcDisc
    Disc0 --> CalcDisc
    CalcDisc --> CapCheck{"discount_amount > 2,000?"}
    CapCheck -- Yes --> CapDisc["discount_amount = 2,000"]
    CapCheck -- No --> Taxable["taxable_amount = subtotal - discount_amount"]
    CapDisc --> Taxable
    Taxable --> TaxLoop["For each item: compute category tax on item gross total<br>Grocery: 5%, Electronics: 12%, Luxury: 18%"]
    TaxLoop --> FinalPayable["final_amount = taxable_amount + total_tax<br>(Final = Subtotal - Discount + Total Tax)"]
    FinalPayable --> DisplayInvoice[/"Print Formatted Itemized Invoice"/]
    DisplayInvoice --> End([End])
```

---

## Case Study 3: Attendance Recovery Computation

```mermaid
flowchart TD
    Start([Start]) --> Input[/"Input total classes held, attended classes"/]
    Input --> CalcCur["current_pct = (attended / total) * 100"]
    CalcCur --> Check75{"current_pct >= 75.0%?"}
    Check75 -- Yes --> Suff[/"Display 'Attendance sufficient (>= 75%)'"/]
    Check75 -- No --> InitExtra["extra = 0"]
    InitExtra --> WhileLoop{"((attended + extra) / (total + extra)) * 100 < 75.0%?"}
    WhileLoop -- Yes --> IncExtra["extra = extra + 1"]
    IncExtra --> WhileLoop
    WhileLoop -- No --> CalcNew["new_pct = ((attended + extra) / (total + extra)) * 100"]
    CalcNew --> DisplayExtra[/"Display extra classes needed and new attendance percentage"/]
    Suff --> End([End])
    DisplayExtra --> End
```

---

## Case Study 4: Warehouse Inventory Reconciliation

```mermaid
flowchart TD
    Start([Start]) --> InitLists["Load parallel lists: items, system_qty, phys_qty<br>Set reorder_level = 20"]
    InitLists --> Header[/"Print Table Header"/]
    Header --> LoopItems{"More items to reconcile?"}
    LoopItems -- Yes --> CalcDiff["diff = phys_qty[i] - system_qty[i]<br>status = ''"]
    CalcDiff --> CheckDiff{"abs(diff) > 5?"}
    CheckDiff -- Yes --> FlagDisc["status += 'DISCREPANCY '"]
    CheckDiff -- No --> CheckReorder
    FlagDisc --> CheckReorder{"phys_qty[i] < reorder_level?"}
    CheckReorder -- Yes --> FlagReorder["status += 'REORDER'"]
    CheckReorder -- No --> CheckOK
    FlagReorder --> CheckOK{"status == ''?"}
    CheckOK -- Yes --> SetOK["status = 'OK'"]
    CheckOK -- No --> PrintRow[/"Print item row with diff and status"/]
    SetOK --> PrintRow
    PrintRow --> LoopItems
    LoopItems -- No --> PrintSummary[/"Print summary metrics: total items, discrepancies, reorders"/]
    PrintSummary --> End([End])
```

---

## Case Study 5: Student Performance Trend Analysis

```mermaid
flowchart TD
    Start([Start]) --> InitData["Define students list, subjects list, 2D marks matrix"]
    InitData --> Header[/"Print Performance Table Header"/]
    Header --> LoopStudents{"More students to process?"}
    LoopStudents -- Yes --> CalcRow["total = sum(marks[i])<br>avg = total / len(subjects)"]
    CalcRow --> CheckExc{"avg >= 80?"}
    CheckExc -- Yes --> GradeExc["grade = 'Excellent'"]
    CheckExc -- No --> CheckGood{"avg >= 60?"}
    CheckGood -- Yes --> GradeGood["grade = 'Good'"]
    CheckGood -- No --> CheckAvg{"avg >= 40?"}
    CheckAvg -- Yes --> GradeAvg["grade = 'Average'"]
    CheckAvg -- No --> GradePoor["grade = 'Poor'"]
    GradeExc --> PrintStudent[/"Print student name, subject marks, average, grade"/]
    GradeGood --> PrintStudent
    GradeAvg --> PrintStudent
    GradePoor --> PrintStudent
    PrintStudent --> LoopStudents
    LoopStudents -- No --> End([End])
```

---

## Case Study 6: Student Timetable Conflict Detection

```mermaid
flowchart TD
    Start([Start]) --> InitTuples["Define timetable list of tuples: (course, start_hour, end_hour)"]
    InitTuples --> SetFlag["conflicts_found = False, count = 0"]
    SetFlag --> OuterLoop{"For i from 0 to len - 1"}
    OuterLoop -- Next i --> InnerLoop{"For j from i + 1 to len - 1"}
    InnerLoop -- Next j --> OverlapCond{"start_a < end_b AND start_b < end_a?"}
    OverlapCond -- Yes --> ReportConflict[/"Print conflict: course A overlaps course B<br>Set conflicts_found = True, count++"/]
    OverlapCond -- No --> InnerLoop
    ReportConflict --> InnerLoop
    InnerLoop -- Done --> OuterLoop
    OuterLoop -- Done --> FinalCheck{"conflicts_found == True?"}
    FinalCheck -- Yes --> PrintCount[/"Display total conflicts count"/]
    FinalCheck -- No --> PrintNone[/"Display 'No conflicts detected'"/]
    PrintCount --> End([End])
    PrintNone --> End
```

---

## Case Study 7: Repeated Transaction Detection

```mermaid
flowchart TD
    Start([Start]) --> InitTx["Load transactions list of tuples: (tx_id, amount, merchant)"]
    InitTx --> InitFlagged["flagged = []"]
    InitFlagged --> LoopI{"For i from 0 to len - 1"}
    LoopI -- Next i --> LoopJ{"For j from i + 1 to len - 1"}
    LoopJ -- Next j --> MatchCond{"amt_a == amt_b AND mer_a == mer_b?"}
    MatchCond -- Yes --> CreatePair["pair = (tid_a, tid_b, amt_a, mer_a)"]
    CreatePair --> InFlagged{"pair in flagged?"}
    InFlagged -- No --> AddFlagged["flagged.append(pair)"]
    InFlagged -- Yes --> LoopJ
    AddFlagged --> LoopJ
    MatchCond -- No --> LoopJ
    LoopJ -- Done --> LoopI
    LoopI -- Done --> CheckResults{"len(flagged) > 0?"}
    CheckResults -- Yes --> DisplayTable[/"Print duplicate transaction pairs table"/]
    CheckResults -- No --> DisplayNone[/"Print 'No repeated transactions found'"/]
    DisplayTable --> End([End])
    DisplayNone --> End
```

---

## Case Study 8: Nested Loop Calendar Generator

```mermaid
flowchart TD
    Start([Start]) --> Input[/"Input month (1-12) and year"/]
    Input --> CalcLeap["is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)"]
    CalcLeap --> CalcDays["Determine total_days in month (29 if Feb & leap, else days[month])"]
    CalcDays --> CalcSakamoto["Compute start weekday using Tomohiko Sakamoto's formula<br>Convert to Monday = 0"]
    CalcSakamoto --> PrintHeader[/"Print Month Header & 'Mon Tue Wed Thu Fri Sat Sun'"/]
    PrintHeader --> InitDay["day = 1"]
    InitDay --> WeekLoop{"For week from 0 to 5"}
    WeekLoop -- Next week --> ColLoop{"For col from 0 to 6"}
    ColLoop -- Next col --> CellIdx["cell = week * 7 + col"]
    CellIdx --> CheckCell{"cell < start OR day > total_days?"}
    CheckCell -- Yes --> PrintSpace[/"Print 5 spaces"/]
    CheckCell -- No --> PrintDay[/"Print formatted day number<br>day = day + 1"/]
    PrintSpace --> ColLoop
    PrintDay --> ColLoop
    ColLoop -- Done --> PrintNL[/"Print newline"/]
    PrintNL --> CheckEnd{"day > total_days?"}
    CheckEnd -- Yes --> End([End])
    CheckEnd -- No --> WeekLoop
```

---

## Case Study 9: Student Marks Matrix Analysis

```mermaid
flowchart TD
    Start([Start]) --> InitMatrix["Define students, subjects, and 2D marks matrix"]
    InitMatrix --> Header[/"Print Table Header"/]
    Header --> RowLoop{"For each student row i"}
    RowLoop -- Next student --> CalcStudent["total = sum(marks[i])<br>avg = total / num_subjects<br>row_totals.append(total)"]
    CalcStudent --> PrintRow[/"Print student name, marks, total, avg"/]
    PrintRow --> RowLoop
    RowLoop -- Done --> ColLoop["For each subject column j:<br>col_sum = sum(marks[i][j])<br>col_avg = col_sum / num_students<br>col_avgs.append(col_avg)"]
    ColLoop --> PrintColAvg[/"Print subject-wise column averages row"/]
    PrintColAvg --> GlobalStats["all_marks = flattened matrix<br>highest = max(all_marks)<br>lowest = min(all_marks)<br>top_student = students[max index in row_totals]<br>best_subject = subjects[max index in col_avgs]"]
    GlobalStats --> PrintSummary[/"Print Highest Mark, Lowest Mark, Top Student, Best Subject"/]
    PrintSummary --> End([End])
```

---

## Case Study 10: Smart Canteen Order and Stock Management

```mermaid
flowchart TD
    Start([Start]) --> InitMenu["Load menu: [name, price, stock]"]
    InitMenu --> ShowMenu[/"Display Canteen Menu with stock"/]
    ShowMenu --> ReadOrderCount[/"Input num_items to order"/]
    ReadOrderCount --> OrderLoop{"More items in order?"}
    OrderLoop -- Yes --> ReadItem[/"Input choice (item number) and qty"/]
    ReadItem --> CheckStock{"menu[choice][2] >= qty?"}
    CheckStock -- Yes --> DeductStock["menu[choice][2] -= qty<br>bill_total += price * qty<br>Record ordered item and qty"]
    CheckStock -- No --> ShowStockErr[/"Display 'Insufficient stock!'"/]
    DeductStock --> OrderLoop
    ShowStockErr --> OrderLoop
    OrderLoop -- Done --> CheckDiscount{"bill_total > 200?"}
    CheckDiscount -- Yes --> ApplyDisc["discount = bill_total * 0.10"]
    CheckDiscount -- No --> NoDisc["discount = 0.0"]
    ApplyDisc --> CalcPayable["payable = bill_total - discount"]
    NoDisc --> CalcPayable
    CalcPayable --> PrintBill[/"Print Itemized Bill, subtotal, discount, payable"/]
    PrintBill --> AuditLoop["Iterate through all menu items:<br>Check if item stock < 5"]
    AuditLoop --> PrintAlerts[/"Print LOW STOCK ALERT for items < 5"/]
    PrintAlerts --> End([End])
```
