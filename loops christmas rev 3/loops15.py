b = int(input("enter a base number:  "))
e = int(input("enter an exponent:  "))
num = 1
for x in range(e):
    num *= b
    
print(num)