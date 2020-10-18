# Define a procedure square(x) that takes a numeric parameter x and returns its square.
# It should have type num -> num. 

def square(x):

    # exception handling
    if not isinstance(x, int) and not isinstance(x, float):
        return "input must be a number"

    return x**2

print(square("two"))
print(square(2))