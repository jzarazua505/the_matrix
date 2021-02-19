def hello(num):
    if num == 0:
        return
    hello(num - 1)
    print("hello")

def power(num, exp):
    if exp == 0:
        return 1
    if num == 0:
        return 0
    if num == 1:
        return 1
    if exp == 1:
        return num
    return num * power(num, exp - 1)

if __name__ == "__main__":
    pass
    
