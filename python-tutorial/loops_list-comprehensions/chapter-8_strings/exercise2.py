# Exercise 8.2
# Think Python
# Chapter 8 - Strings
# Exercise 2

# There is an error in the following program. When the letter is 'Q', the output is 'Qack'.
# Modify the program to fix the error.

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     print letter + suffix

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'Q':
        letter = 'Qu'
    print (letter + suffix)