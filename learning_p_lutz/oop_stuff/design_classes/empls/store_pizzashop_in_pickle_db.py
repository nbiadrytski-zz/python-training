from learning_p_lutz.oop_stuff.design_classes.empls.pizzashop_has_a_composition import PizzaShop
import pickle


shop = PizzaShop()

print(shop.server)  # <Employee: name=Pat Server, salary=40000>
print(shop.chef)  # <Employee: name=Teddy Robot, salary=50000>

pickle.dump(shop, open('shopfile.pkl', 'wb'))  # stores an entire composite shop object in a file all at once

obj = pickle.load(open('shopfile.pkl', 'rb'))

print(obj.server)  # <Employee: name=Pat Server, salary=40000>
print(obj.chef)  # <Employee: name=Teddy Robot, salary=50000>

obj.order('Dan')
# Dan orders from <Employee: name=Pat Server, salary=40000>
# Teddy Robot makes pizza
# oven bakes
# Dan pays for item to <Employee: name=Pat Server, salary=40000>
