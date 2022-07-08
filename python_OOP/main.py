from item import Item

item1 = Item("MyItem", 750)

# Setting an attribute
#item1.name = "OtherItem"

# Geting the attribute
#print(item1.name)

print(item1.price)
item1.apply_increase(0.2)
item1.apply_discount()
print(item1.price)






