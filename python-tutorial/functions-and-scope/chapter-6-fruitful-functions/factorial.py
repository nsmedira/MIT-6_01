def factorial(n):

    # create indentation to debug
    space = ' ' * (4 * n)

    # show what the function is doing
    print (space, 'factorial', n)

    # this function requires integer input
    if not isinstance(n, int):
        print ('Factorial is only defined for integers')
        return None

    # the integer needs to be positive
    if n < 0:
        print ('Factorial is not defined for negative integers.')
        return None

    if n == 0:

        # show what the function is returning
        print (space, 'returning 1')

        return 1

    else :

        # this can be reduced
        # recurse = factorial(n-1)
        # result = n * recurse
        # return result

        result = n * factorial(n-1)

        # show what the function is returning
        print (space, 'returning', result)

        # return n * factorial(n-1)
        return result
        

# print (factorial(25))