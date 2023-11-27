fin = open("C:\\Users\\19RMcClean.ACC\\Downloads\\shelley.txt")
lines = 0
for line in fin:
    lines = lines + 1

fin.close()
print(lines)

