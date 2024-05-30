from receipt import Receipt
from order import Order
from menu import MenuItem


def discount_sandwich(order):
    if order.items.get(menu["Sandwich"], 0) >= 5:
        return 0.1
    return 0


def discount_salad(order):
    if order.items.get(menu["Soup"], 0) > 0:
        return 0.1
    return 0


def discount_soup(order):
    if order.items.get(menu["Sandwich"], 0) > 0 and order.items.get(menu["Salad"], 0) > 0:
        return 0.2
    return 0


# Define the menu
menu = {
    "Sandwich": MenuItem("Sandwich", 10, discount_sandwich, 10),
    "Salad": MenuItem("Salad", 8, discount_salad, 8),
    "Soup": MenuItem("Soup", 6, discount_soup, 15),
    "Coffee/tea": MenuItem("Coffee/tea", 5, None, 5)
}


def main():
    name = input("Enter your name: ")
    order = Order()

    for item_name, item in menu.items():
        quantity = int(input(f"Enter quantity for {item_name} (${item.price}): "))
        order.add_item(item, quantity)

    Receipt.print_receipt(name, order)


main()
