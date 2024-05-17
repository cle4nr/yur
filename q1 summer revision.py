numlist = []
for x in range(5):
    numinput = int(input("enter a number "))
    numlist.append(numinput)
print(numlist)

numlist = [x+1 for x in numlist]
print(numlist)