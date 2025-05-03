class Discount:
    def calculate(self, customer_type):
        if customer_type == "regular":
            return 10
        elif customer_type == "vip":
            return 20

class DiscountOcp:
    def calculate(self):
        pass

class RegularDiscount(DiscountOcp):
    def calculate(self):
        return 10

class VIPDiscount(DiscountOcp):
    def calculate(self):
        return 20

def get_discount(discount: DiscountOcp):
    return discount.calculate()
