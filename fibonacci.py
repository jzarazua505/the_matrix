num1 = 0
num2 = 1
print(num1)
for x in range(9):
    temp = num1 + num2
    num1 = num2
    num2 = temp
    print(num1)
