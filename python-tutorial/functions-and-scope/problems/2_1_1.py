# Part 1

# num
def a(x):
    return x + 1

# 2. num
def b(x):
    return x + 1.0

# 3. (assume x and y are ints or floats) num
def c(x, y):
    return x + y

# 4. bool
def d(x, y):
    return x > y

# 5. bool
def e(x, y, z):
    return x >= y and x <= z

# 6. NoneType (trick question: there is no return statement)
def f(x, y):
    x + y - 2


# Part 2 - provide the type and value of the expressions being evaluated
# if evaluating an expression would cause an error, select NoneType and write error in the box
# if the value of an expression is a function, select function as the type

# 1. num
a(6)

# 2. num
a(-5.3)

# 3. num
a(a(a(6)))

# 4. num
c(a(1), b(1))

# 5. bool
d(10, 11.1)

# 6. bool
e(a(3), b(4), c(3, 4))

# 7. func
e