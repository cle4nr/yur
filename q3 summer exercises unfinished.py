rainfallwk = []
for x in range(7):
    rnapnd = int(input("how much rainfall: "))
    rainfallwk.append(rnapnd)

print(rainfallwk)
print("total rainfall:",sum(rainfallwk))
avgrn = sum(rainfallwk) / 7
roundedavg = round(avgrn,1)
print("average rainfall:",roundedavg)

for i in (rainfallwk):
    if i > 3.5:
        print("on day",i,"the rainfall exceeded 3.5cm")

        