# Exercise 8.1
# Think Python
# Chapter 8 - Strings
# Exercise 1

# Write a function that takes a string as an argument and displays the letters backward, one per line.

def reverse_string(str):

    i = -1
    while abs(i) <= len(str):
        print(str[i])
        i -= 1

reverse_string('Supercalifragilisticexpialidocious')