# (1 + 2 + 3 + 4 + 5) + 6 + 7 + 8 + 9 + 10 = ?
# sum = 0
# for x in range(1, 11):
#     sum += x
# print(sum)


def factorial(input):
    product = 1
    for x in range(1, input + 1):
        product *= x
    return product

def recursive_factorial(input):
    if input == 1:
        return input
    return input * recursive_factorial(input - 1)


fact_sum = factorial(5) + factorial(4) + factorial(2)
print(fact_sum)
