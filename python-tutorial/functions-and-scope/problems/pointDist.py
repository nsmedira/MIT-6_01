# Define a procedure pointDist(x1, y1, x2, y2) that returns the distance between a point
# in two-dimensional space with coordinates x1, y1 and another point with coordinates
# x2, y2. Use math.sqrt (of type num -> float). Your function should have type (num, num,
# num, num) -> float. 

import inspect, math

def pointDist(x1, y1, x2, y2):

    # exception handling
    args = locals()
    for point in args:
        if not isinstance(args[point], int):
            return "each coordinate must be of type int"

    return float(math.sqrt((x1-x2)**2 + (y1-y2)**2))

print(pointDist(9, 7, 3, 2))