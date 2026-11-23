"""
Case Study 10: Smart Canteen Order and Stock Management
Concepts Used: Nested Lists (mutable menu table), Enumerate, Loops, Conditionals, Stock Deduction.
"""
import sys

def get_input(prompt=""):
    val = input(prompt)
    if not sys.stdin.isatty():
        print(val)
    return val

def main():
    print("=" * 45)
    print("          SMART CANTEEN MENU")
    print("=" * 45)

    # Menu structure: [item_name, price, stock_quantity]
    menu = [
        ["Idli",       20,  50],
        ["Dosa",       30,  40],
        ["Sambar",     10,  80],
        ["Tea",         8, 100],
        ["Coffee",     12,  60],
        ["Rice Meal",  60,  20]
    ]

    for i, item in enumerate(menu):
        print(f"{i+1}. {item[0]:<14} Rs.{item[1]:>4}   Stock: {item[2]:>3}")
    print("=" * 45)

    order_items = []
    order_qty = []
    bill_total = 0.0

    num_items = int(get_input("\nHow many items to order? "))
    for _ in range(num_items):
        choice = int(get_input("Item number: ")) - 1
        qty = int(get_input("Quantity: "))

        if 0 <= choice < len(menu):
            if menu[choice][2] >= qty:
                order_items.append(menu[choice][0])
                order_qty.append(qty)
                menu[choice][2] -= qty
                bill_total += menu[choice][1] * qty
            else:
                print(f"Insufficient stock for {menu[choice][0]}! (Available: {menu[choice][2]})")
        else:
            print("Invalid item choice!")

    # Bulk discount: 10% discount if bill total exceeds Rs. 200
    discount = bill_total * 0.10 if bill_total > 200 else 0.0
    payable = bill_total - discount

    print("\n" + "=" * 45)
    print("               ORDER BILL")
    print("=" * 45)
    for i in range(len(order_items)):
        print(f"{order_items[i]:<25} x{order_qty[i]}")
    print("-" * 45)
    print(f"{'Subtotal':<25} Rs.{bill_total:>8.2f}")
    if discount > 0:
        print(f"{'Discount (10%)':<25}-Rs.{discount:>8.2f}")
    print(f"{'PAYABLE AMOUNT':<25} Rs.{payable:>8.2f}")
    print("=" * 45)

    # Low Stock Audit: Alert if any item has fewer than 5 units left
    print("\n--- LOW STOCK ALERT REPORT ---")
    alert = False
    for item in menu:
        if item[2] < 5:
            print(f"  [ALERT] {item[0]}: only {item[2]} unit(s) remaining!")
            alert = True
    if not alert:
        print("  All canteen items are adequately stocked.")
    print("=" * 45)

if __name__ == "__main__":
    main()
