from datetime import datetime

def get_valid_input(prompt, valid_options=None, input_type=str):
    while True:
        user_input = input(prompt)
        try:
            if input_type == int:
                user_input = int(user_input)
            if valid_options and user_input not in valid_options:
                raise ValueError("Invalid option selected.")
            return user_input
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_receipt(name, items, total_price, gst, final_amount):
    print("=" * 27, "Hari Supermarket", "=" * 30)
    print(" " * 31, "Kanekal")
    print(f"Name: {name} {' ' * 30} Date: {datetime.now()}")
    print("-" * 75)
    print(f"{'S.No':<5}{'Items':<20}{'Quantity':<10}{'Price':<10}")
    for i, (item, quantity, price) in enumerate(items, 1):
        print(f"{i:<5}{item:<20}{quantity:<10}{price:<10}")
    print("-" * 75)
    print(f"{'Total Amount:':<50} Rs {total_price}")
    print(f"{'GST Amount:':<50} Rs {gst}")
    print("-" * 75)
    print(f"{'Final Amount:':<50} Rs {final_amount}")
    print("-" * 75)
    print(" " * 20, "Thanks for visiting!")
    print("-" * 75)

def main():
    name = input("Enter your name: ")

    items = {
        'Rice': 20,
        'Sugar': 30,
        'Salt': 20,
        'Oil': 80,
        'Paneer': 110,
        'Maggi': 50,
        'Boost': 90,
        'Colgate': 85
    }

    item_list = "\n".join([f"{item:<10} Rs {price}/unit" for item, price in items.items()])
    print("Available items:\n", item_list)

    purchased_items = []
    total_price = 0

    while True:
        option = get_valid_input("Enter item name to purchase or 'done' to finish: ", valid_options=list(items.keys()) + ['done'], input_type=str).capitalize()
        if option == 'Done':
            break
        quantity = get_positive_integer(f"Enter quantity for {option}: ")
        price = items[option] * quantity
        purchased_items.append((option, quantity, price))
        total_price += price

    if total_price > 0:
        gst = total_price * 0.05
        final_amount = total_price + gst
        display_receipt(name, purchased_items, total_price, gst, final_amount)
    else:
        print("No items purchased, billing canceled.")

if __name__ == "__main__":
    main()
