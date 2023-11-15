#program 3
print("this program returns the highest number out of 3 that you enter")

a = int(input("enter a number:	 "))      
b = int(input("enter a number:	 "))
c = int(input("enter a number:	 "))

def highest(a,b,c):
    maximum = a
    if b > maximum:
        maximum = b
        return(b)
    elif c > maximum:
        maximum = c
        return(c)
print((highest(a,b,c)),"is the greatest number")

