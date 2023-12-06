n = int(input("Enter a natural number: "))
if n < 0:
    n = int(input("Enter a natural number(positive integer): "))


fact = 1
for x in range(1,n+1):
    fact = fact*x
    
print(fact)