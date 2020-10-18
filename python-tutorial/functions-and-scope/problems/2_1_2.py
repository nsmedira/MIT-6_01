# Provide the type and value of the expressions being evaluated

# If evaluating an expression would cause an error,
# select noneType and write error in the box

# If the value of an expression is a function,
# select function as the type and write function in the box.

# 1. 
# type = num
# value = 4
# notes: the function has access to the global variables defined in __main__. a = 10 at the beginning is red herring
a = 10
def f(x):
    return x + a
a = 3
f(1)

# 2.
# type = num
# value = 19
x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)

print(g(x))