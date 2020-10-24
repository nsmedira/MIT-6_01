import math

def quadraticRoots(a, b, c):

    if a == 0:

        # bx + c = 0
        # bx = -c
        # x = -c / b
        return ( c * -1 ) / b

    else:

        # create an empty list
        roots = []

        b = -1 * b
        bac = math.sqrt(b ** 2 - 4 * a * c)
        a = (2 * a)

        # root 1
        roots.append(
            (b + bac) / a
        )

        # root 2
        roots.append(
            (b - bac) / a
        )

        return roots