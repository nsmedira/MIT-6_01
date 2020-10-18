# Define a procedure evalQuadratic(a, b, c, x) that returns the value of the quadratic 
# ax2 + bx + c. Your function should have type (num, num, num, num) -> num. 

def evalQuadratic(a, b, c, x):

    # exception handling
    args = locals()
    for point in args:
        if not isinstance(args[point], int):
            return "each argument must be of type int"

    return a * x**2 + b * x + c

print(evalQuadratic(6, 11, 35, 100))