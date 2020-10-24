import math

def quadraticRootsComplex(a, b, c):

    if a == 0:

        # bx + c = 0
        # bx = -c
        # x = -c / b
        return ( c * -1 ) / b

    else:

        # create an empty list
        roots = []

        b = -1 * b
        bac = b ** 2 - 4 * a * c
        
        # handle complex solutions
        if bac < 0:
            sqrt_bac = complex(0, math.sqrt(bac * -1))
        else:
            sqrt_bac = math.sqrt(bac)

        a = (2 * a)

        # root 1
        roots.append(
            (b + sqrt_bac) / a
        )

        # root 2
        roots.append(
            (b - sqrt_bac) / a
        )

        return roots

# complex solution
print(quadraticRootsComplex(1, 2, 3))

# real solution
print(quadraticRootsComplex(1, 3, -4))