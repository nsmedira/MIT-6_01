# 1. Type these functions into a file named palindrome.py and test them out. What happens if you call middle with a string with two letters? One letter? What about the empty string, which is written '' and contains no letters?

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print('result of palindrome with 2 letter string:', middle('to'))

print('result of palindrome with 1 letter string:', middle('a'))

print('result of palindrome with 0 letter string:', middle(''))

# 2. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(str):

    # palindrome if first and last letters are the same and the middle is a palindrome

    # has to be at least 2 letters
    if len(str) < 2:
        return False

    # if first and last don't match, return false
    if first(str) != last(str):
        return False

    if len(str) == 2 and first(str) == last(str):
        return True

    if len(str) == 3:
        if first(str) == last(str):
            return True
        else:
            return False
    
    return is_palindrome(middle(str))


print(is_palindrome('tattarrattat'))