rainfallwk = []
for x in range(7):
    rnapnd = int(input("how much rainfall: "))
    rainfallwk.append(rnapnd)

print(rainfallwk)
print("total rainfall:",sum(rainfallwk))
avgrn = sum(rainfallwk) / 7
roundedavg = round(avgrn,1)
print("average rainfall:",roundedavg)
daycount =0
for i in (rainfallwk):
    daycount += 1
    if i > 3.5:
        print("on day",daycount,"the rainfall exceeded 3.5cm by",i-3.5)
        

        