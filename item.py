import csv
from winreg import HKEY_LOCAL_MACHINE

from itsdangerous import want_bytes

class Item:
    '''Class attribute, accessible from all instances'''
    pay_rate = 0.8 # The pay rate after a 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0!"
        
        # Assign to self object
        self.__name = name 
        # leading single underscore = semiprivate
        # leading double underscore = immutable & private
        self.__price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    
    def calculate_total_price(self):
        return self.__price * self.quantity
    
        
    '''Make instantiate_from_csv a @classmethod because it cannot accept 'self' as an argument. 
    Can only be called from the class, not an instance.
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
    
    '''Where @classmethod passes the class through as the first arg, 
    @staticmethod leaves arguments open.
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
    '''
    @classmethod and @staticmethod can both be called from instances,
    but there is no real reason for that in a normal context, so they 
    should basically always be called from the class itself if used correctly.
    Ex: Item.is_an_integer(num), Item.instantiate_from_csv()
    '''
        
    def __repr__(self):
        # For parent/child classes, self.__class__.__name__ will display the name of the class in case of a child
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    @property
    # @property decorator = Read Only Attribute
    def name(self):
        # cannot return self.name
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("Name must be 10 characters or less!")
        else:
            self.__name = new_name
            
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise Exception("Price must be a positive number")
        else:
            self.__price = new_price
        
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        
    ''' Abstraction - using dunder prefix for methods to obscure from users: '''
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.name} {self.quantity} times.
        Regards, Seani Wan
        """
        
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('smtp')
        self.__prepare_body()
        self.__send()
        
    # send_email() uses the __methods (abstraction) so that
    # the user can call send_email(), but none of the 
    # abstracted methods