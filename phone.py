from item import Item


class Phone(Item): # Phone class = child, Item class = parent
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to 0!"
        
        self.broken_phones = broken_phones