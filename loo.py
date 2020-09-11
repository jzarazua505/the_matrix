# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

tri_size = int(input("How big do you want the triangle? "))

for x in range(1, tri_size + 1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()

# for m in range(1, 7):
#     for n in range(1, 6):
#         print(f"{m},{n}", end=" ")
#     print()
    