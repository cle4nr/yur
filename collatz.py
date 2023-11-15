number = int(input("Enter a number:\n"))
def collatz(n):
    if number %2 == 0:
        return(n//2)
    else:
        return(3*n+1)

while number != 1:
    number = collatz(number);print(number)
