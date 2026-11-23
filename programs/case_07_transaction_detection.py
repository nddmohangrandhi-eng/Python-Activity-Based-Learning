"""
Case Study 7: Repeated Transaction Detection
Concepts Used: Tuples, Lists, Nested Loops, Tuple Unpacking, Duplicate Detection.
"""

def main():
    print("=" * 58)
    print("       REPEATED TRANSACTION DETECTION REPORT")
    print("=" * 58)

    # Tuples: (transaction_id, amount, merchant)
    transactions = [
        ("T001", 500.00, "Amazon"),
        ("T002", 1200.00, "Flipkart"),
        ("T003", 500.00, "Amazon"),
        ("T004", 750.00, "Swiggy"),
        ("T005", 1200.00, "Flipkart"),
        ("T006", 300.00, "Zomato"),
        ("T007", 500.00, "Amazon")
    ]

    flagged = []
    # O(n^2) pairwise comparison to detect duplicate charges
    for i in range(len(transactions)):
        tid_a, amt_a, mer_a = transactions[i]
        for j in range(i + 1, len(transactions)):
            tid_b, amt_b, mer_b = transactions[j]
            # Flag if same amount and same merchant appear
            if amt_a == amt_b and mer_a == mer_b:
                pair = (tid_a, tid_b, amt_a, mer_a)
                if pair not in flagged:
                    flagged.append(pair)

    if flagged:
        print(f"{'TxID-1':<8}{'TxID-2':<8}{'Amount':>10}   {'Merchant':<12} {'Status'}")
        print("-" * 58)
        for f in flagged:
            print(f"{f[0]:<8}{f[1]:<8}{f[2]:>10.2f}   {f[3]:<12} *** DUPLICATE")
    else:
        print("No repeated transactions found.")

    print("=" * 58)
    print(f"Total Repeated Pairs Flagged: {len(flagged)}")
    print("=" * 58)

if __name__ == "__main__":
    main()
