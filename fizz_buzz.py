# print numbers 1-100 
# fizz if divisible 3
# buzz if divisible 5
# fizzbuzz if both
# print eash thing on new line

def make_output(num, num_words):
    output = ""
    for div in num_words:
        if num % div == 0:
            output += num_words[div]
    if output == "":
        output = num
    return output

def fizz_buzz2(start, stop):
    whatever = {
        3: "fizz",
        5: "buzz",
        7: "fuzz",
        10: "bizz"
    }
    for num in range(start, stop + 1):
        print(make_output(num, whatever))

def fizz_buzz(x, y):
    for num in range(x, y):
        output = ""
        if num % 3 == 0:
            output += "fizz"
        if num % 5 == 0:
            output += 'buzz'
        if num % 7 == 0:
            output += "fuzz"
        if output == "":
            output = num
        print(output)

def old_fizz_buzz(x,y):
    for num in range(x, y):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

if __name__ == "__main__":
    fizz_buzz(1, 101)
    # fizz_buzz2(1, 100)