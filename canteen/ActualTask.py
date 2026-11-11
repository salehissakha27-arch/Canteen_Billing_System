def display_menu():
    print("----- CANTEEN MENU -----")
    print("1. Burger - Rs. 50")
    print("2. Pizza - Rs. 80")
    print("3. Coffee - Rs. 30")
    print("4. Sandwich - Rs. 40")


def generate_bill(items, discount_percentage=0):
    total = 0

    prices = {
        "Burger": 50,
        "Pizza": 80,
        "Coffee": 30,
        "Sandwich": 40
    }

    for item, quantity in items.items():
        total += prices[item] * quantity

    tax = total * 0.05
    discount = (total + tax) * discount_percentage / 100
    final_amount = total + tax - discount

    print("\n----- FINAL BILL -----")
    print("Total:", total)
    print("Tax:", tax)
    print("Discount:", discount)
    print("Final Amount:", final_amount)
