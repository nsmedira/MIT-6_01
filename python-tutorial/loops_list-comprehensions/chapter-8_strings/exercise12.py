# ROT13 is a weak form of encryption that involves “rotating” each letter in a word by 13 places1. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.

# Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount.

# For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.

# You might want to use the built-in functions ord, which converts a character to a numeric code, and chr, which converts numeric codes to characters.

def rotate_word(string, integer):

    string = string.lower()
    
    new = ''

    lower_bound = ord('a')
    upper_bound = ord('z')

    for letter in string:
        c = ord(letter) + integer
        if c < lower_bound:
            c = upper_bound - (lower_bound - c) + 1
        elif c > upper_bound:
            c = lower_bound + (c - upper_bound) - 1
        new += chr(c)

    return new

print(rotate_word('MElon', -10))