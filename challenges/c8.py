"""
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay. 
"""

price = input("How much did the bill cost? ")
price = int(price)
diners = input("How many people are eating with you including yourself?" )
diners = int(diners)
priceeach = price/diners
print("everyone pays",priceeach)