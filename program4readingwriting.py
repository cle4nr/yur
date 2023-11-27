fin = open("C:\\Users\\19RMcClean.ACC\\Downloads\\shelley.txt")
lines = 0
elines = 0
for line in fin:
    if "" in line:
        lines = lines + 1
    else:
        elines = elines + 1

        

fin.close()
print(lines)
print(elines)


