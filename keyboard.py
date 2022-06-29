from item import Item


class Keyboard(Item): # Phone class = child, Item class = parent
    # can adjust class variables for children:
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)