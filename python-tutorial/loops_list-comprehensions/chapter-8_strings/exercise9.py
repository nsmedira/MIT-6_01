# use slice and step size to make a one-line version of is_palindrome

def is_palindrome(word):
    return word == word[::-1] 


print(is_palindrome('tattarrattat'))