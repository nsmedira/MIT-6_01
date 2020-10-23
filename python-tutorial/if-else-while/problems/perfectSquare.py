import math

def perfectSquare(n):

    if not isinstance(n, int) or n <= 0:
        return "argument must be a positive integer"

    if n == 1:
        return True

    # assuming that this problem wants a loop instead of the square root function

    i = math.floor(n/2)
    while i > 1:
        if i ** 2 == n:
            return True
        i -= 1

    return False