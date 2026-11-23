# Test Cases and Verification Suite

This document contains the test case matrices, boundary conditions, and mathematical verification for all 10 case studies in the **Python Activity-Based Learning** project.

> **Note on Verification Scope**:  
> The sample execution for each case study has been executed and verified in the terminal environment. The additional test cases documented below represent theoretical validation matrices and edge-case formulas designed to confirm algorithmic soundness across different input boundaries.

---

## Case Study 1: Employee Payroll and Deduction Analysis

### Logic & Slabs
- HRA: 20% of basic pay
- DA: 10% of basic pay
- Overtime: Rs. 500/hr
- Progressive Income Tax Slabs:
  - Gross <= Rs. 50,000: 0%
  - Gross Rs. 50,001 - 1,00,000: 5%
  - Gross Rs. 1,00,001 - 1,50,000: 10%
  - Gross > Rs. 1,50,000: 15%
- Statutory Deductions: PF = 12% of basic pay, Other = Rs. 2,000 (fixed)

### Test Matrix
| Test Case ID | Description | Basic Pay | OT Hrs | Incentive | Expected Gross | Tax Slab | Expected Tax | Expected PF | Other | Expected Net | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01-A** | Low salary (no tax) | Rs. 35,000 | 0 | Rs. 0 | Rs. 45,500.00 | 0% | Rs. 0.00 | Rs. 4,200.00 | Rs. 2,000 | Rs. 39,300.00 | Expected |
| **TC-01-B** | Boundary at Rs. 50k | Rs. 38,461.54 | 0 | Rs. 0 | Rs. 50,000.00 | 0% | Rs. 0.00 | Rs. 4,615.38 | Rs. 2,000 | Rs. 43,384.62 | Expected |
| **TC-01-C** | Mid salary (5% slab) | Rs. 50,000 | 10 | Rs. 5,000 | Rs. 75,000.00 | 5% | Rs. 3,750.00 | Rs. 6,000.00 | Rs. 2,000 | Rs. 63,250.00 | Expected |
| **TC-01-D** | Sample Run (10% slab) | Rs. 75,000 | 10 | Rs. 5,000 | Rs. 107,500.00 | 10% | Rs. 10,750.00 | Rs. 9,000.00 | Rs. 2,000 | Rs. 85,750.00 | **Verified (Run)** |
| **TC-01-E** | High salary (15% slab) | Rs. 120,000 | 20 | Rs. 10,000 | Rs. 176,000.00 | 15% | Rs. 26,400.00 | Rs. 14,400.00 | Rs. 2,000 | Rs. 133,200.00 | Expected |

---

## Case Study 2: Retail Billing with Multiple Discount Rules

### Calculation Policy (Tax & Discount Order)
- **Category Tax**: Calculated on individual pre-discount item gross totals (`item_total = quantity * price`):
  - Grocery: 5%
  - Electronics: 12%
  - Luxury: 18%
  - `total_tax = sum(item_tax)`
- **Invoice Discount**: Calculated on subtotal threshold:
  - Subtotal > Rs. 10,000: 10%
  - Subtotal > Rs. 5,000: 5%
  - Subtotal <= Rs. 5,000: 0%
  - Maximum discount capped at Rs. 2,000.
- **Payable Policy**: The discount is applied to the subtotal (`taxable_subtotal = subtotal - discount`), and total tax is added:
  $$\text{Final Payable Amount} = (\text{Subtotal} - \text{Discount}) + \text{Total Tax}$$

### Test Matrix
| Test Case ID | Description | Products (Qty x Price, Category) | Subtotal | Disc % | Discount | Taxable | Total Tax | Final Payable | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-02-A** | Low subtotal (no discount) | Rice (2 x 500, Grocery), Cable (1 x 1000, Electronics) | Rs. 2,000.00 | 0% | Rs. 0.00 | Rs. 2,000.00 | Rs. 170.00 | Rs. 2,170.00 | Expected |
| **TC-02-B** | Boundary at Rs. 5,000 | Groceries (5 x 1000, Grocery) | Rs. 5,000.00 | 0% | Rs. 0.00 | Rs. 5,000.00 | Rs. 250.00 | Rs. 5,250.00 | Expected |
| **TC-02-C** | Sample Run (5% discount) | Rice (2x250, Groc), Headphone (1x3500, Elec), Perfume (2x1800, Lux) | Rs. 7,600.00 | 5% | Rs. 380.00 | Rs. 7,220.00 | Rs. 1,093.00 | Rs. 8,313.00 | **Verified (Run)** |
| **TC-02-D** | High tier (10% discount) | Tablet (2 x 6000, Electronics) | Rs. 12,000.00 | 10% | Rs. 1,200.00 | Rs. 10,800.00 | Rs. 1,440.00 | Rs. 12,240.00 | Expected |
| **TC-02-E** | Discount Cap Enforcement | Luxury Watch (1 x 25000, Luxury) | Rs. 25,000.00 | 10% | Rs. 2,000.00 (capped) | Rs. 23,000.00 | Rs. 4,500.00 | Rs. 27,500.00 | Expected |

---

## Case Study 3: Attendance Recovery Computation

### Logic
- Threshold: 75.00%
- Current attendance: `(attended / total) * 100`
- While `((attended + extra) / (total + extra)) * 100 < 75.0`: `extra += 1`

### Test Matrix
| Test Case ID | Description | Total Held | Attended | Current % | Extra Needed | Projected Attended / Total | New Attendance % | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-03-A** | Sample Run (Recovery needed) | 60 | 38 | 63.33% | 28 | 66 / 88 | 75.00% | **Verified (Run)** |
| **TC-03-B** | Sufficient attendance | 50 | 40 | 80.00% | 0 | 40 / 50 | 80.00% | Expected |
| **TC-03-C** | Exactly 75% boundary | 40 | 30 | 75.00% | 0 | 30 / 40 | 75.00% | Expected |
| **TC-03-D** | Low attendance recovery | 80 | 45 | 56.25% | 60 | 105 / 140 | 75.00% | Expected |
| **TC-03-E** | Zero attendance edge case | 10 | 0 | 0.00% | 30 | 30 / 40 | 75.00% | Expected |

---

## Case Study 4: Warehouse Inventory Reconciliation

### Logic
- Discrepancy alert: `abs(physical - system) > 5`
- Low stock reorder alert: `physical < 20`

### Test Matrix
| Test Case ID | Item | System Qty | Physical Qty | Difference | Discrepancy Alert? | Reorder Alert? | Expected Status | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-04-A** | Rice Bags | 150 | 143 | -7 | Yes (`abs(-7) > 5`) | No (`143 >= 20`) | `DISCREPANCY` | **Verified (Run)** |
| **TC-04-B** | Sugar | 80 | 85 | +5 | No (`abs(5) <= 5`) | No (`85 >= 20`) | `OK` | **Verified (Run)** |
| **TC-04-C** | Oil Cans | 45 | 38 | -7 | Yes (`abs(-7) > 5`) | No (`38 >= 20`) | `DISCREPANCY` | **Verified (Run)** |
| **TC-04-D** | Wheat | 200 | 200 | 0 | No (`0 <= 5`) | No (`200 >= 20`) | `OK` | **Verified (Run)** |
| **TC-04-E** | Salt | 30 | 18 | -12 | Yes (`abs(-12) > 5`) | Yes (`18 < 20`) | `DISCREPANCY REORDER` | **Verified (Run)** |

---

## Case Study 5: Student Performance Trend Analysis

### Logic
- Average: `sum(marks) / len(subjects)`
- Grade thresholds: `>= 80`: Excellent, `>= 60`: Good, `>= 40`: Average, `< 40`: Poor.

### Test Matrix
| Test Case ID | Student | Maths | Physics | Chemistry | Python | Total | Average | Expected Grade | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-05-A** | Ananya | 85 | 72 | 68 | 91 | 316 | 79.0 | Good | **Verified (Run)** |
| **TC-05-B** | Bharath | 55 | 48 | 62 | 70 | 235 | 58.8 | Average | **Verified (Run)** |
| **TC-05-C** | Chitra | 38 | 45 | 50 | 42 | 175 | 43.8 | Average | **Verified (Run)** |
| **TC-05-D** | High Boundary (80.0) | 80 | 80 | 80 | 80 | 320 | 80.0 | Excellent | Expected |
| **TC-05-E** | Poor Boundary (<40.0) | 35 | 30 | 28 | 38 | 131 | 32.8 | Poor | Expected |

---

## Case Study 6: Student Timetable Conflict Detection

### Logic
- Overlap condition: `start_a < end_b and start_b < end_a`

### Test Matrix
| Test Case ID | Interval A | Interval B | Overlap Condition Check | Expected Result | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-06-A** | Mathematics (09:00-10:00) | Chemistry (09:00-11:00) | `9 < 11 and 9 < 10` -> True | **CONFLICT** | **Verified (Run)** |
| **TC-06-B** | Physics (10:00-11:00) | Chemistry (09:00-11:00) | `10 < 11 and 9 < 11` -> True | **CONFLICT** | **Verified (Run)** |
| **TC-06-C** | Python Lab (14:00-16:00) | English (15:00-16:00) | `14 < 16 and 15 < 16` -> True | **CONFLICT** | **Verified (Run)** |
| **TC-06-D** | Mathematics (09:00-10:00) | Physics (10:00-11:00) | `9 < 11 and 10 < 10` -> False | **NO CONFLICT** | Expected |
| **TC-06-E** | Chemistry (09:00-11:00) | Python Lab (14:00-16:00) | `9 < 16 and 14 < 11` -> False | **NO CONFLICT** | Expected |

---

## Case Study 7: Repeated Transaction Detection

### Logic
- Transaction format: `(transaction_id, amount, merchant)`
- Flagged if `amt_a == amt_b and mer_a == mer_b` for any pair `j > i`.

### Test Matrix
| Test Case ID | Tx 1 | Tx 2 | Matching Criteria | Duplicate Pair Created | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-07-A** | T001 (500, Amazon) | T003 (500, Amazon) | Amount=500, Merchant=Amazon | `(T001, T003, 500.0, Amazon)` | **Verified (Run)** |
| **TC-07-B** | T001 (500, Amazon) | T007 (500, Amazon) | Amount=500, Merchant=Amazon | `(T001, T007, 500.0, Amazon)` | **Verified (Run)** |
| **TC-07-C** | T002 (1200, Flipkart) | T005 (1200, Flipkart) | Amount=1200, Merchant=Flipkart | `(T002, T005, 1200.0, Flipkart)` | **Verified (Run)** |
| **TC-07-D** | T003 (500, Amazon) | T007 (500, Amazon) | Amount=500, Merchant=Amazon | `(T003, T007, 500.0, Amazon)` | **Verified (Run)** |
| **TC-07-E** | T004 (750, Swiggy) | T006 (300, Zomato) | Amount differs, Merchant differs | Not Flagged | Expected |

---

## Case Study 8: Nested Loop Calendar Generator

### Logic
- Leap year rule: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`
- Weekday calculation: Tomohiko Sakamoto's formula mapped to Monday = 0.

### Test Matrix
| Test Case ID | Input Month & Year | Leap Year? | Total Days | Expected Start Day | Calendar Alignment | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-08-A** | July 2025 | No | 31 | Tuesday (col 1) | Day 1 under Tue, Day 6 under Sun | **Verified (Run)** |
| **TC-08-B** | February 2024 | Yes (Leap) | 29 | Thursday (col 3) | 29 days rendered correctly | Expected |
| **TC-08-C** | February 2025 | No | 28 | Saturday (col 5) | Exactly 28 days rendered | Expected |
| **TC-08-D** | January 2024 | Yes | 31 | Monday (col 0) | Starts at column index 0 | Expected |
| **TC-08-E** | December 2025 | No | 31 | Monday (col 0) | Full 31 days with proper wrap | Expected |

---

## Case Study 9: Student Marks Matrix Analysis

### Logic
- 2D nested list with row totals, row averages, column averages, global max/min, top student, and best subject.

### Test Matrix
| Metric / Calculation | Target Field | Expected Value | Actual Run Value | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **Row Total & Avg** | Arun (88, 76, 65, 92) | Total: 321, Avg: 80.2 | Total: 321, Avg: 80.2 | **Verified (Run)** |
| **Row Total & Avg** | Bala (55, 60, 72, 48) | Total: 235, Avg: 58.8 | Total: 235, Avg: 58.8 | **Verified (Run)** |
| **Row Total & Avg** | Divya (91, 85, 88, 95) | Total: 359, Avg: 89.8 | Total: 359, Avg: 89.8 | **Verified (Run)** |
| **Row Total & Avg** | Esha (70, 55, 60, 75) | Total: 260, Avg: 65.0 | Total: 260, Avg: 65.0 | **Verified (Run)** |
| **Col Avg (Maths)** | (88 + 55 + 91 + 70) / 4 | 76.0 | 76.0 | **Verified (Run)** |
| **Col Avg (Science)** | (76 + 60 + 85 + 55) / 4 | 69.0 | 69.0 | **Verified (Run)** |
| **Col Avg (English)** | (65 + 72 + 88 + 60) / 4 | 71.2 | 71.2 | **Verified (Run)** |
| **Col Avg (Python)** | (92 + 48 + 95 + 75) / 4 | 77.5 | 77.5 | **Verified (Run)** |
| **Global Highest** | `max(all_marks)` | 95 (Divya - Python) | 95 | **Verified (Run)** |
| **Global Lowest** | `min(all_marks)` | 48 (Bala - Python) | 48 | **Verified (Run)** |
| **Top Student** | Highest row total | Divya (359) | Divya (359) | **Verified (Run)** |
| **Best Subject** | Highest column average | Python (77.5) | Python (77.5) | **Verified (Run)** |

---

## Case Study 10: Smart Canteen Order and Stock Management

### Logic
- Menu inventory decrement on purchase.
- Bulk order discount: 10% if subtotal > Rs. 200.
- Low stock warning: `stock < 5`.

### Test Matrix
| Test Case ID | Action / Order | Subtotal | Discount | Payable | Ending Stock | Low Stock Triggered? | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-10-A** | Sample Run: 4 x Rice Meal (Rs. 60), 3 x Dosa (Rs. 30) | Rs. 330.00 | Rs. 33.00 (10%) | Rs. 297.00 | Rice Meal: 16, Dosa: 37 | No (All items >= 5) | **Verified (Run)** |
| **TC-10-B** | Order <= Rs. 200 (No discount) | 2 x Dosa (Rs. 60), 2 x Tea (Rs. 16) = Rs. 76.00 | Rs. 0.00 | Rs. 76.00 | Dosa: 38, Tea: 98 | No | Expected |
| **TC-10-C** | Deplete stock to trigger alert (< 5) | Order 18 Rice Meals (from 20 stock) | Rs. 1080.00 | Rs. 108.00 | Rice Meal: 2 remaining | Yes (`Rice Meal: only 2 left!`) | Expected |
| **TC-10-D** | Order exceeding available stock | Order 50 Rice Meals (when stock is 20) | - | - | - | "Insufficient stock!" alert | Expected |
