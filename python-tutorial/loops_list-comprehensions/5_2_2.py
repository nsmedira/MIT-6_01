import math

def perpDist(p, line):

    # return the unsigned (positive) distance between
    # a point in two-dimensional space with coordinates p = (px, py)
    # and a line with equation ax + by + c == 0, 
    # where 1 = (a, b, c)

    # modification: change 1 parameter to line

    # use math.sqrt ( type num -> float )
    # your function should have type (num, num), (num, num, num) -> float

    # distance between a point and a line

    # check input typing
    number_types = (int, float, complex)
    if (
        not isinstance(p, tuple) 
        or not isinstance(line, tuple)
        or not len(p) == 2
        or not len(line) == 3
        or not isinstance(p[0], number_types)
        or not isinstance(p[1], number_types)
        or not isinstance(line[0], number_types)
        or not isinstance(line[1], number_types)
        or not isinstance(line[2], number_types)
    ):
        return 'arguments must have type (num, num), (num, num, num)'

    x, y, a, b, c = p[0], p[1], line[0], line[1], line[2]

    return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    print(perpDist((0,0), (3, 4, -6, -5)))