# Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.

# we need the math library
import math

def hypotenuse ( a, b ):

    # pythagorean theorem (c is hypotenuse)
    # a**2 + b**2 = c**2

    # c = sqrt(a**2 + b**2)

    return math.sqrt(a**2 + b**2)

print (hypotenuse (2,4))