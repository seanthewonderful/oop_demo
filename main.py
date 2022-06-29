from item import Item
from phone import Phone


item1 = Item("MyItem", 750)
item1.name = "OtherItem"
# item1.price = 700.99
item1.apply_discount()
print(item1.price)










# Item.instantiate_from_csv()
# print(Item.all)

# computer = Item("Comp1", 800, 3)
# phone1 = Phone("sFone1.0", 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone("sFone2.0", 700, 5, 1)

# print(Item.all)
# print(Phone.all)


# n='7.5'
# print(Item.is_an_integer(n))
# print(n.is_integer())

# Item.instantiate_from_csv()
# for instance in Item.all:
#     print(instance.name)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

'''See all attributes in the class/instance'''
# print(Item.__dict__)
# print(item1.__dict__)



