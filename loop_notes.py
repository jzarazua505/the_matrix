# for x in range(11):
#     print(x)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

row = ""
for x in range(1, 6):
    row += f"{x} "
    print(row)

row = ""  # ""

x = 1
row += f"{x} " # row = "" + "1 " = "1 "
print(row)

x = 2
row += f"{x} " # row = "1 " + "2 " = "1 2 "
print(row)

x = 3
row += f"{x} " # row = "1 2 " + "3 " = "1 2 3 "
print(row)

x = 4
row += f"{x} " # row = "1 2 3 " + "4 " = "1 2 3 4 "
print(row)

for x in range(1, 6):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()

x = 0
while True:
    print(x)
    x += 1 
