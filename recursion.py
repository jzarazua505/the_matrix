def hello(num):
    if num == 0:
        return
    hello(num - 1)
    print("hello")

hello(0)
