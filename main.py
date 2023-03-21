from item import Item
from phone import Phone
from keyboard import Keyboard


####################################################################################################################
## 6. Object Oriented Programming Principles

''' (1) Encapsulation '''

# item1 = Item('MyItem', 750, 6)

# print(item1.price)
# item1.apply_increment(0.2)
# print(item1.price)
# item1.apply_discount()
# print(item1.price)

''' (2) Abstraction '''

# # item1.connect('google_smtp') # AttributeError
# # item1.prepare_body()         # AttributeError
# # item1.send()                 # AttributeError

# # item1.__connect('google_smtp') # AttributeError
# # item1.__prepare_body()         # AttributeError
# # item1.__send()                 # AttributeError

# item1.send_email()

''' (3) Inheritance '''

# phone1 = Phone('jscPhone', 1000, 3)

# print(phone1.price)
# phone1.apply_increment(0.2)
# print(phone1.price)

''' (4) Polymorphism
Polymorphism in action, a single function does now
how to handle different kinds of objects as expected!
'''
##########################################
## Example
name = 'Jim' # str
print(len(name))

some_list = ['some', 'name'] # list
print(len(some_list))
##########################################

keyboard1 = Keyboard('jscKeyboard', 500, 3)

print(keyboard1.price)
keyboard1.apply_discount()
print(keyboard1.price)


####################################################################################################################
## 5. Encapsulation: Properties, Getters, Setters

# Item.instantiate_from_csv()
# print(Item.all)

# item1 = Item('MyItem', 750)

###########################

# item1._name = 'OtherItem'
# print(item1._name)

###########################

# item1.__name = 'OtherItem' # After Modifying
# print(item1.__name)        # NO Error

###########################
                             # Without Modifying
# # print(item1.__name)      # AttributeError

###########################

## Getting Attribute: @property
# print(item1.name)

## Setting Attribute: @name.setter
# item1.name = 'OtherItem'
# print(item1.name)

# # item1.name = 'Hello World' 
# # print(item1.name)


####################################################################################################################
## 4. Inheritance

# phone1 = Item('jscPhoneV10', 500, 5)
# phone1.broken_phones = 1
# phone2 = Item('jscPhoneV20', 700, 5)
# phone2.broken_phones = 1

## After creating sub-class Phone

# phone1 = Phone('jscPhoneV10', 500, 5)
# phone1.broken_phones = 1
# phone2 = Phone('jscPhoneV20', 700, 5)
# phone2.broken_phones = 1

# phone1 = Phone('jscPhoneV10', 500, 5, 1)
# phone2 = Phone('jscPhoneV20', 700, 5, 1)
# print(phone1.calculate_total_price())
# print(phone2.calculate_total_price())

# item1 = Item('Phone', 100, 1)
# phone1 = Phone('jscPhoneV10', 500, 5, 1)
# print(Item.all)
# print(Phone.all)

####################################################################################################################
## 3. Class Methods, Static Methods

# item1 = Item('Phone', 100, 1)
# item2 = Item('Laptop', 1000, 3)
# item3 = Item('Cable', 10, 5)
# item4 = Item('Mouse', 50, 5)
# item5 = Item('Keyboard', 75, 5)
# print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(3))
# print(Item.is_integer(7.5))

###############################################################
## When to use class methods and when to use static methods? ##
###############################################################
## def instancemethod():
'''
This should do something that must be unique per instance!
'''

## @classmethod
'''
This should do something that has a relationship with the class,
but usually, those are used to manipulate different structures of data
to instantiate objects, like we have done with CSV.
'''

## @staticmethod
'''
This should do something that has a relationship with the class,
but NOT something that must be unique per instance.
'''

## Summing Up with Relationship!
## Instance Method: Class X, (Single)   Instance  O
## Class Method   : Class O, (Multiple) Instances O
## Static Method. : Class O,            Instance  X


####################################################################################################################
## 2. Constructor: __init__

# item1 = Item('Phone', 100, 1)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# item2 = Item('Laptop', 1000, 3)

# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# print(Item.__dict__)  # All the attributes for Class level
# print(item1.__dict__) # All the attributes for Instance level
# print(item2.__dict__) # All the attributes for Instance level

# print(item1.pay_rate)
# print(item1.price)
# item1.apply_discount()
# print(item1.pay_rate)
# print(item1.price)

# print(item2.pay_rate)
# print(item2.price)
# # # item2.pay_rate = 0.7   # pay_rate      : NameError
# # Item.pay_rate = 0.7    # Item.pay_rate : Class Level
# item2.pay_rate = 0.7     # self.pay_rate : Instance Level
# item2.apply_discount()
# print(item2.pay_rate)
# print(item2.price)
# print(item1.pay_rate)

# item3 = Item('Cable', 10, 5)
# item4 = Item('Mouse', 50, 5)
# item5 = Item('Keyboard', 75, 5)
# for instance in Item.all:
#     print(instance.name)
# print(Item.all)


####################################################################################################################
## 1. Getting started

# item1 = Item()
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 1

# print(type(item1))          # <class '__main__.Item'>
# print(type(item1.name))     # <class 'str'>
# print(type(item1.price))    # <class 'int'>
# print(type(item1.quantity)) # <class 'int'>

# item2 = Item()
# item2.name = 'Laptop'
# item2.price = 1000
# item2.quantity = 3

# print(item2))
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_price(item1.price, item1.quantity))
# print(item2.calculate_total_price(item2.price, item2.quantity))