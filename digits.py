ans = "y"
while ans == "y":
    num = int(input("what is the number of your choosing? "))
    count = 0
    while num != 0:
        num //= 10
        count += 1
    print(f"Total digits are: {count}")
    ans = input("would you like to give another number (y/n)? ")

# or

# num = input("what is the number? ")
# print(len(num))
