# The mean (or average) of a list of n numbers is the sum of 
# the numbers divided by n. For example, the mean of 
# 2, 7, 3, 9, and 13 is (2+7+3+9+13)/5, or 6.8. 
# Write a procedure mean that takes as input a list of numbers 
# (of any length) and returns the mean. It should have type 
# list(num) -> float.

# One thing to watch out for is an empty list as input. 
# It's not clear that any numeric answer makes sense here. 
# You should just return None

# You can implement this as an extremely short procedure 
# if you use the Python built-in procedures sum, which returns 
# the sum of the elements of a list, and len, which returns 
# the length of a list.

# If your procedure says that the mean of 1 and 2 is 1, 
# rather than 1.5, then you've been tricked by Python's 
# division (/) operation. Be careful. 

def mean (t):

    # check type
    if (
        not isinstance(t, list)
    ): return 'argument must be a list'

    # if argument is a list, make sure it isn't empty
    if len(t) == 0: return None

    # if argument list has values
    number_types = int, float, complex
    for i in t:
        if not isinstance(i, number_types):
            return 'all elements in the input list must be numbers'

    return sum(t) / len(t)

if __name__ == "__main__":
    print(mean([1, 2]))
    print(mean([2, 7, 3, 9, 13]))