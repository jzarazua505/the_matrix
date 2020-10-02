print(__name__)

from export_test import other_function
from prime import prime_numbers

if __name__ == "__main__":
    print("import_test.py is the __main__ script!")
    other_function()
    prime_numbers(0, 36)
