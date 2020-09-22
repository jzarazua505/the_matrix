integer = int(input("What is the number?"))
reverse_number = 0
print("Given Number ", integer)

while integer > 0:
    remainder = integer % 10
    reverse_number = (reverse_number * 10) + remainder
    integer = integer // 10

print("Reversed Number ", reverse_number)
