#program 2
print("this program returns the highest number out of 3 that you enter")

a = int(input("enter a number:	 "))      
b = int(input("enter a number:	 "))
c = int(input("enter a number:	 "))

def highest(a,b,c):
    if a>b:
        if a>c:
            print((a),"is the greatest number")
        else:
            print((c),"is the greatest number")
    else:
        if b>c:
            print((b),"is the greatest number")
        else:
            print((c),"is the greatest number")   
highest(a,b,c)
