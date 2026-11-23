"""
Case Study 4: Warehouse Inventory Reconciliation
Concepts Used: Lists, For Loop, Conditionals, Absolute Value Function, String Formatting.
"""

def main():
    print("=" * 65)
    print("        WAREHOUSE INVENTORY RECONCILIATION REPORT")
    print("=" * 65)

    items = ["Rice Bags", "Sugar", "Oil Cans", "Wheat", "Salt"]
    system_qty = [150, 80, 45, 200, 30]
    phys_qty = [143, 85, 38, 200, 18]
    reorder_level = 20

    print(f"{'Item':<14}{'System':>8}{'Physical':>10}{'Diff':>8}  {'Status':<20}")
    print("-" * 65)

    discrepancy_count = 0
    reorder_count = 0

    for i in range(len(items)):
        diff = phys_qty[i] - system_qty[i]
        status = ""

        # Flag discrepancy if absolute difference exceeds 5 units
        if abs(diff) > 5:
            status += "DISCREPANCY "
            discrepancy_count += 1

        # Flag reorder if physical quantity is below reorder threshold
        if phys_qty[i] < reorder_level:
            status += "REORDER"
            reorder_count += 1

        if status == "":
            status = "OK"

        print(f"{items[i]:<14}{system_qty[i]:>8}{phys_qty[i]:>10}{diff:>8}  {status.strip()}")

    print("=" * 65)
    print(f"Total Items Evaluated : {len(items)}")
    print(f"Discrepancies Flagged : {discrepancy_count}")
    print(f"Items Below Reorder   : {reorder_count}")
    print("=" * 65)

if __name__ == "__main__":
    main()
