# Implement a procedure stddev that takes a list of numbers 
# as argument and returns the standard deviation. If the list 
# has fewer than 2 elements, then the standard deviation 
# should be 0.0. (Actually, if we want to be correct, the 
# standard deviation of a list of 0 or 1 elements isn't 
# defined, but returning 0.0 is okay for now.) 

# The standard deviation of a list of n numbers is the square 
# root of the following quantity: 
# 1/(n-1) times the sum of (xi - m)2, where xi ranges over 
# the elements of the list and m is the mean of the list. 
# It is a measure of how much variation there is from the mean. 

# You should try to write the procedure so that it uses list 
# comprehension rather than an explicit loop. You should also 
# use your mean procedure from the previous problem. In order 
# to do that, include that code again (together with your new 
# code) in the box below. In general, you can enter more than 
# one procedure definition in the tutor code boxes, and the 
# tutor does not remember code from one problem to the next. 

# To compute the square root of a number, you can simply raise 
# the number to the power of 0.5 using Python's exponentiation 
# operator **. Alternatively, you can use the Python sqrt 
# procedure, but you'll need to import it from the math 
# package. In order to do that include 

# from math import sqrt 

# as the first line your code

def stddev(t):

    # check type
    if (
        not isinstance(t, list)
    ): return 'argument must be a list'

    # if argument is a list, make sure it has more than 1 element
    if len(t) < 2: return 0.0

    n = len(t)
    m = sum(t) / n
    u = [(x-m)**2 for x in t]

    return ((1/n) * sum(u))**0.5

if __name__ == "__main__":

    # checked against https://www.mathsisfun.com/data/standard-deviation-formulas.html
    print(stddev([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]))

    # checked against https://www.mathsisfun.com/data/standard-deviation.html
    print(stddev([600, 470, 170, 430, 300]))