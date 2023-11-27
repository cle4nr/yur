fin = open("C:\\Users\\19RMcClean.ACC\\Downloads\\numbers.txt")
total = 0
for line in fin:
    x=line.strip()
    if x != "":
        x = int(x)
        total = total +x
    
fin.close()
print(total)
