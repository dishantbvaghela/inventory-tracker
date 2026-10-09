import json
import os

FILE = "inventory.json"
LOW_STOCK_LIMIT = 50


def load_items():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_items(items):
    with open(FILE, "w") as f:
        json.dump(items, f, indent=2)


def add_stock(items):
    name = input("Item name: ").strip()
    qty = int(input("Quantity to add: "))
    items[name] = items.get(name, 0) + qty
    save_items(items)
    print("Saved.")


def remove_stock(items):
    name = input("Item name: ").strip()
    if name not in items:
        print("Item not found.")
        return
    qty = int(input("Quantity to remove: "))
    items[name] = max(0, items[name] - qty)
    save_items(items)
    print("Saved.")


def show_items(items):
    if not items:
        print("Inventory is empty.")
        return
    for name, qty in items.items():
        alert = "  <-- LOW STOCK" if qty < LOW_STOCK_LIMIT else ""
        print(f"{name}: {qty}{alert}")


def delete_item(items):
    name = input("Item name to delete: ").strip()
    if name in items:
        del items[name]
        save_items(items)
        print("Deleted.")
    else:
        print("Item not found.")

def reorder_list(items):
    low = {name: qty for name, qty in items.items() if qty < LOW_STOCK_LIMIT}
    if not low:
        print("All items are well stocked.")
        return
    print("Items to reorder:")
    for name, qty in low.items():
        needed = LOW_STOCK_LIMIT - qty
        print(f"{name}: {qty} left (order at least {needed} more)")        

def main():
    items = load_items()
    while True:
        print("\n1. Add stock\n2. Remove stock\n3. View all\n4. Delete item\n5. Reorder list\n6. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_stock(items)
        elif choice == "2":
            remove_stock(items)
        elif choice == "3":
            show_items(items)
        elif choice == "4":
            delete_item(items)
        elif choice == "5":
            reorder_list(items)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


main()      
