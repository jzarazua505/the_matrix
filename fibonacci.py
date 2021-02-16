def fibo(index):
    num1 = 0
    num2 = 1
    print(num1)
    for _ in range(index):
        temp = num1 + num2
        num1 = num2
        num2 = temp
        print(num1)

def r_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return r_fibo(n - 1) + r_fibo(n - 2)

fibo(11)
