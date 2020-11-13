def myRange(n):

    # Write a procedure, called myRange, that takes a single positive 
    # integer n as an argument and returns a list with 
    # elements starting with 0 and going up through n - 1. 
    # Don't use range! Use a while loop. 

    # check type
    if not isinstance(n, int) or not n > 0:
        return 'argument must be a positive integer'

    t = []
    i = 0
    while i < n:
        t += [i]
        i += 1

    return t

if __name__ == "__main__":
    print(myRange(1.0))