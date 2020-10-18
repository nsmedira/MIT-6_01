# A number, a, is a power of b if it is divisible by b and a/b is a power of b. 

# assumptions: 
# asking if a is a NON-NEGATIVE, INTEGER POWER
# a is EVENLY divisible by b

# Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.

def is_power(a, b):

    # any number to the 0 power is 1
    if a == 1:
        return True
    
    # if a ==  b, a is the 1st power of b
    if a == b:
        return True

    # if a is evenly divisble by b, perform is_power again (base cases above haven't been met)
    if a % b == 0:
        return is_power(a/b, b)

    # if none of the above is true, return false
    return False

print (is_power(2**0, 2))