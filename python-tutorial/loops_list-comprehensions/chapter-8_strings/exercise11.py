# The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).

# the function does not do what its name suggests because if the first letter in the string is not lowercase, it returns False
def any_lowercase1(s):

    # for every letter c in string s
    for c in s:

        # if c is a lower case letter
        if c.islower():

            # return True
            return True

        # if c is not a lower case letter
        else:

            # return False
            return False


# this function will always return hardcoded string 'True' (instead of boolean True) on the first iteration through the loop because it is checking the lowercase status of hardcoded string 'c'
def any_lowercase2(s):

    # for every letter c in string s
    for c in s:

        # if the string 'c' is lowercase
        if 'c'.islower():

            # return the string 'True'
            return 'True'

        # if the string 'c' is not lowercase
        else:

            # return the string 'False'
            return 'False'

# this function will return a boolean value that represents whether the last character in the string is lowercase or not
def any_lowercase3(s):

    # for every letter c in string s
    for c in s:

        # set flag True if c is lowercase, False if not
        flag = c.islower()

    # return flag
    return flag

# this function will return True if any of the letters in the string are lowercase
def any_lowercase4(s):

    # set flag = False
    flag = False

    # for every letter c in string s
    for c in s:
    
        # set flag = False unless c is lowercase
        flag = flag or c.islower()

    # return flag
    return flag

# this function returns False if the string contains any uppercase letters. if all letters are lowercase, it returns True
def any_lowercase5(s):

    # for every letter c in string s
    for c in s:

        # if c is not a lowercase letter
        if not c.islower():

            # return False
            return False

    # if we make it through the entire loop, return True
    return True