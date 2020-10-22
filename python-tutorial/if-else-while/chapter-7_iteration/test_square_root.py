from square_root import square_root
import math

def test_square_root():
    a = 1.0
    while a < 10:
        places = 11

        value = round(square_root(a), places)
        test = round(math.sqrt(a), places)
        diff = abs(test - value)

        value = str(value)
        spaces = ' ' * (13 - len(value))
        value += spaces

        test = str(test)
        spaces = ' ' * (13 - len(test))
        test += spaces

        print(a, value, test, str(diff))
        a += 1.0

test_square_root()