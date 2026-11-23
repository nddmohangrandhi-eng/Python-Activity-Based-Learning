"""
Case Study 2: Retail Billing with Multiple Discount Rules
Concepts Used: Lists, Loops (for), Conditionals (if-elif-else), Arithmetic Operators, String Formatting.

Calculation Policy:
- Category-specific sales taxes (Grocery 5%, Electronics 12%, Luxury 18%) are calculated
  on the pre-discount item gross totals (quantity * unit price).
- Tiered discounts (5% if subtotal > Rs. 5,000; 10% if subtotal > Rs. 10,000; capped at Rs. 2,000)
  are evaluated on the invoice subtotal.
- Final Payable Amount = (Subtotal - Discount Amount) + Total Tax.
"""
import sys

def get_input(prompt=""):
    val = input(prompt)
    if not sys.stdin.isatty():
        print(val)
    return val

def main():
    print("=" * 60)
    print("       RETAIL BILLING & INVOICE MANAGEMENT SYSTEM")
    print("=" * 60)

    products = []
    categories = []
    quantities = []
    prices = []

    num_products = int(get_input("Enter number of products: "))
    for i in range(num_products):
        print(f"\nProduct {i+1}:")
        products.append(get_input("  Product name: "))
        categories.append(get_input("  Category (Grocery/Electronics/Luxury): "))
        quantities.append(int(get_input("  Quantity: ")))
        prices.append(float(get_input("  Unit price: ")))

    # Calculate Subtotal (sum of pre-discount item totals)
    subtotal = 0.0
    for i in range(num_products):
        subtotal += quantities[i] * prices[i]

    # Determine Discount based on subtotal thresholds:
    # > Rs. 10,000 : 10%
    # > Rs. 5,000  : 5%
    # Otherwise    : 0%
    if subtotal > 10000:
        discount_percent = 10
    elif subtotal > 5000:
        discount_percent = 5
    else:
        discount_percent = 0

    discount_amount = subtotal * (discount_percent / 100)
    # Enforce maximum discount limit of Rs. 2,000
    if discount_amount > 2000:
        discount_amount = 2000.0

    taxable_amount = subtotal - discount_amount

    # Calculate category-specific tax per product on pre-discount item totals:
    # Grocery: 5%, Electronics: 12%, Luxury: 18%
    total_tax = 0.0
    item_taxes = []
    for i in range(num_products):
        item_total = quantities[i] * prices[i]
        cat = categories[i].strip().capitalize()
        if cat == "Grocery":
            tax_rate = 0.05
        elif cat == "Electronics":
            tax_rate = 0.12
        elif cat == "Luxury":
            tax_rate = 0.18
        else:
            tax_rate = 0.05  # Default fallback rate

        item_tax = item_total * tax_rate
        item_taxes.append(item_tax)
        total_tax += item_tax

    # Final Payable: Taxable Subtotal + Total Tax
    final_amount = taxable_amount + total_tax

    # Display Itemized Invoice
    print("\n" + "=" * 60)
    print("                  RETAIL INVOICE")
    print("=" * 60)
    print(f"{'Product':<20}{'Qty':>5}{'Price':>10}{'Total':>10}{'Tax':>10}")
    print("-" * 60)
    for i in range(num_products):
        item_total = quantities[i] * prices[i]
        print(f"{products[i]:<20}{quantities[i]:>5}{prices[i]:>10.2f}{item_total:>10.2f}{item_taxes[i]:>10.2f}")
    print("-" * 60)
    print(f"{'Subtotal':<45}{subtotal:>10.2f}")
    print(f"{'Discount (' + str(discount_percent) + '%)':<45}{-discount_amount:>10.2f}")
    print(f"{'Total Tax':<45}{total_tax:>10.2f}")
    print("=" * 60)
    print(f"{'FINAL PAYABLE AMOUNT':<45}{final_amount:>10.2f}")
    print("=" * 60)

if __name__ == "__main__":
    main()
