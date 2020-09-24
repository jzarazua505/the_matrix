size = int(input("How big do you want your triangle? "))
for x in range(size):
    for y in range(x + 1):
        print("*", end=" ")
    print()
for x in range(size - 1, 0, -1):
    for y in range(x):
        print("*", end=" ")
    print()
