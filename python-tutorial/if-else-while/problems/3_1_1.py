def a(x, y, z):
    if x: 
        return y
    else:
        return z

def b(y, z):
    return a(y>z, y, z)

# value: 3
# type: int
a(False, 2, 3)

# value: 3
# type: int
b(3,2)

# value: the a() function
# type: function
# print(a(3>2, a, b))

# value: error, cannot compare functions 
# type: NoneType
# print(b(a, b))