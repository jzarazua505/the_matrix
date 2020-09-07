list1 = [12, 15, 32, 42, 55, 180, 75, 122, 200, 150]
for x in list1:
    if x > 150:
        continue
    
    if int(x / 5) == x / 5:
        print(x)

for x in list1:
    if x > 150:
        break
    if x % 5 == 0:
        print(x)
        