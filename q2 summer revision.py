hours = [ 12, 7, 9, 9, 6, 8, 2]
hours = [x*0.5 for x in hours]
hours = [x*1.35 for x in hours]
sumh = sum(hours)
roundedsumh = round(sumh,1)
print(roundedsumh,'€')