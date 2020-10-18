# Define a procedure perpDist(px, py, a, b, c) that returns the unsigned (positive)
# distance between a point in two-dimensional space with coordinates px, py and a line
# with equation ax + by + c == 0. Use math.sqrt (of type num -> float). Your function
# should have type (num, num, num, num, num) -> float. 

# We don't necessarily expect you to remember or rederive this formula; try Google if
# you need help. You might find the function abs useful. 

import math

def perpDist(px, py, a, b, c):

    # exception handling
    args = locals()
    for point in args:
        if not isinstance(args[point], int):
            return "each argument must be of type int"

    return float(
        abs(a * px + b * py + c)
        / math.sqrt(a**2 + b**2)
    )

# check https://brilliant.org/wiki/dot-product-distance-between-point-and-a-line/
print(perpDist(-3, 2, 2, 4, -5))

print(3/(2 * math.sqrt(5)))