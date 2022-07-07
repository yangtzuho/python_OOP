from item import Item

class Phone(Item):
    #all = []
    def __init__(self, name:  str, price: float, quantity = 0, broken_phone = 0) -> None:
        # Call to super function to have access to all attributes / methods
        super().__init__(
                name, price, quantity  
                )
        # Rum validations to the received arguments

        assert broken_phone >= 0, f"Broken_phone  {broken_phone} is not greater than zero!" 

        # Assign to self object

        self.broken_phone = 1

        # Actions to excute
        #Phone.all.append(self)
