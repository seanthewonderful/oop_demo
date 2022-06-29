import csv

class Item:
    '''Class attribute, accessible from all instances'''
    pay_rate = 0.8 # The pay rate after a 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    '''Make instantiate_from_csv a @classmethod because it cannot accept 'self' as an argument. 
    Can only be called from the class, not an instance'''
    '''
    @classmethod should do something that has a relationship with the class,
    but usually those are used to manipulate different structures of the data
    to instantiate objects, like we have done with CSV
    '''
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    '''Where @classmethod passes the class through as the first arg, @staticmethod leaves arguments open'''
    '''
    @staticmethod should do something that has a relationship with the class, 
    but not something that must be unique per instance!
    '''
    @staticmethod
    def is_an_integer(num):
        # We will count out the floats (ending in .0)
        # ex: 5.0, 10,0, ...
        if isinstance(num, float):
            # Count out the floats (ending in .0)
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
n='7.5'
print(Item.is_an_integer(n))
print(n.is_integer())

# Item.instantiate_from_csv()
# for instance in Item.all:
#     print(instance.name)

# print(Item.all)
    
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
''' To Demonstrate that all types are classes, and creating a class makes a new type '''
# print(type(item1), type(item1.name), type(item1.price))
''' Can add unique attributes to individual instances - "Instance Attribute" '''
# item2.has_numpad = False
'''See all attributes in the class/instance'''
# print(Item.__dict__)
# print(item1.__dict__)



