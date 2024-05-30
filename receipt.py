import datetime


class Receipt:
    @staticmethod
    def print_receipt(name, order):
        total, max_prep_time = order.calculate_total()
        tax = total * 0.16
        grand_total = total + tax
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("*************************************************")
        print(f"{name}, thanks for your order")
        print("Items        qty  Price")

        for item, quantity in order.items.items():
            item_total = item.price * quantity * (1 - item.get_discount(order))
            print(f"{item.name:<12} {quantity:<3}  ${item_total:.2f}")

        print(f"Tax             ${tax:.2f}")
        print(f"Total           ${grand_total:.2f}")
        print(f"{date}, Your order will be ready in {max_prep_time} minutes")
        print("*************************************************")
