class MenuItem:
    def __init__(self, name, price, discount_condition, prep_time):
        self.name = name
        self.price = price
        self.discount_condition = discount_condition
        self.prep_time = prep_time

    def get_discount(self, order):
        if self.discount_condition:
            return self.discount_condition(order)
        return 0
