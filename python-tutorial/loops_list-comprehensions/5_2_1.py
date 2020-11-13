import math

def pointDist(p1: tuple, p2: tuple) -> float:

    # return the distance between a point in two-dimensional
    # space with coordinates p1 = (x1, y1)
    # and another point with coordinates p2 = (x2, y2)
    # use math.sqrt (of type num -> float)
    # your function should have type (num, num), (num, num) -> float

    # distance between two points: https://www.mathsisfun.com/algebra/distance-2-points.html

    # check input typing
    number_types = (int, float, complex)
    if (
        not isinstance(p1, tuple) 
        or not isinstance(p2, tuple)
        or not len(p1) == 2
        or not len(p2) == 2
        or not isinstance(p1[0], number_types)
        or not isinstance(p1[1], number_types)
        or not isinstance(p2[0], number_types)
        or not isinstance(p2[1], number_types)
    ):
        return 'arguments must be tuples of 2 numbers'

    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

if __name__ == "__main__":
    print(pointDist((3, 2), (9, 7)))