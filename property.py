width = 5
height = 2
# This is where we calculate perimeter
perimeter = 2 * (width + height)
# This is where we calculate area
area = width * height
print("Perimeter is " + str(perimeter) + " and Area is " + str(area) + "!")
print(f"Perimeter is {perimeter} and Area is {area}!")
print(f"Area: {area}")

# f(x) = y = 2x + 4
# f(input) = 2 * (input) + 4 = output
def f(x):
    return 2 * x + 4

y = f(6)
print(y)

def get_area(width, height):
    return width * height

print()
area1 = get_area(5, 2)
print(f"Area 1: {area1}")
area2 = get_area(7, 8)
print(f"Area 2: {area2}")
print()

test = "julian"

def print_words():
    print("words")
    print("stuff")
    print("thing")
    return "test"

test = print_words()

print(test)
other = print_words()
print_words()
print_words()
print_words()
