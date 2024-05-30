class Order:

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def calculate_total(self):
        total = 0
        max_prep_time = 0
        for item, quantity in self.items.items():
            discount = item.get_discount(self)
            total += item.price * quantity * (1 - discount)
            max_prep_time = max(max_prep_time, item.prep_time)
        return total, max_prep_time
