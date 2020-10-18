# Define a procedure odd(x) that returns True when its integer argument is an odd
# number and False otherwise. It should have type int -> boolean. Use the % (mod)
# operator, not if. 

def odd(x):

    # exception handling
    if not isinstance(x, int):
        return "input must be of type 'int'"
    
    return x % 2 != 0