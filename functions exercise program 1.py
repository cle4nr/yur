#program 1
print("this program returns the highest number out of 3 that you enter")

a = int(input("enter a number:	 "))      
b = int(input("enter a number:	 "))
c = int(input("enter a number:	 "))

def highest(a,b,c):
    if a>b and a>c:
        return(a)
    elif b>a and b>c:
        return(b)
    else:
        return(c)
    
print(highest(a,b,c))
##