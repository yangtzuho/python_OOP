import csv
class Item:
    pay_rate = 0.8 # The pay rate 
    all = []
    def __init__(self, name:  str, __price: float, quantity = 0) -> None:
        # Rum validations to the received arguments
        assert __price >= 0, f"__price {__price} is not greater than zero!"
        assert quantity >= 0, f"Quentity {quantity} is not greater than zero!"

        # Assign to self object
        self.__name  = name
        self.__price = __price 
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate 

    def apply_increase(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def name(self):
        print("You are trying to get an attribute")
        return self.__name

    @name.setter
    def name(self, value):
        print("You are trying to set the attribute")
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total___price(self):
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Item(
                    name=item.get('name'),
                    __price=float(item.get('__price')),
                    quantity=float(item.get('quantity'))
                    )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e : 5.0 10.0
        if isinstance(num, float): 
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}, {self.__price}, {self.quantity}')"


    