import queue


class Item:
    def __init__(self, name:  str, price: float, quantity = 0) -> None:
        # Rum validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quentity {quantity} is not greater than zero!"
        # Assign to self object
        self.name  = name
        self.price = price 
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, -1)

item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price(), item2.calculate_total_price())

