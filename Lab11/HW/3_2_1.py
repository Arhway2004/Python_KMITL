class StationaryGood:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_cost(self):
        return self.price

class Magazine(StationaryGood):
    def __init__(self, name, price):
        super().__init__(name, price)

class Book(StationaryGood):
    def __init__(self, name, price):
        discounted_price = price * 0.9
        super().__init__(name, discounted_price)

class Ribbon(StationaryGood):
    def __init__(self, name, length_in_meters, price_per_meter):
        self.length_in_meters = length_in_meters
        cost = length_in_meters * price_per_meter
        super().__init__(name, cost)

def getTotalCost(basket):
    total_cost = 0
    for item in basket:
        total_cost += item.get_cost()
    return total_cost

basket = [
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Book("Windows 7 for Beginners", 200),
    Book("Windows 7 for Beginners", 200),
    Ribbon("Blue Ribbon", 10, 5),
]

total_cost = getTotalCost(basket)

print(f"Total cost of goods in the basket: {total_cost} Bahts")
