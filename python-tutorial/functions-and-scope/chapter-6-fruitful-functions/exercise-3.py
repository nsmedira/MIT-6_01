# Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.

def is_between(x, y, z):
    if x <= y and y <= z :
        return True
    else :
        return False

print ( is_between (4, 3, 4))