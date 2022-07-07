class Item:
    def __init__(self, name) -> None:
        self.name  = name
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone")
item1.price = 100
item1.quantity = 5

item2 = Item("Laptop")
item2.price = 1000
item2.quantity = 3

print(item1.name, item2.name)