def prime_numbers(start, stop):
    print(f"Prime numbers between {start} and {stop} are:")
    for x in range(start, stop + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            print(x)

if __name__ == "__main__":
    prime_numbers(30000, 30500)
