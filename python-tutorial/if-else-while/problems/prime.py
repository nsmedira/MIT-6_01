import math

def prime(n):

    if not isinstance(n, int) or n <= 0:
        return "argument must be a positive integer"

    # a number is prime if i can only be divided by itself and 1
    
    # write a loop that tries to divide n by all integers between floor(n/2) and 1
    i = math.floor(n/2)
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    
    return True