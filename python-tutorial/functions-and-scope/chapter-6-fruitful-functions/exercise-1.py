# Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.

def x_compared_y ( x, y ):
    if x > y :
        return 1
    if x == y :
        return 0
    if x < y :
        return -1

print(x_compared_y(2, 3))