def main():
    n_items = int(input("Enter the number of items: "))
    total = 0

    for i in range(n_items):
        print("\nItem", i + 1)

        item_name = input("Enter item name: ")
        unit_price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))
        extended_price = unit_price * quantity
        total += extended_price

        print("Item Name:", item_name)
        print(f"Unit Price: ${unit_price:.2f}")
        print("Quantity:", quantity)
        print(f"Extended Price: ${extended_price:.2f}")
    print(f"\nTotal: ${total:.2f}")

if __name__ == "__main__":
    main()