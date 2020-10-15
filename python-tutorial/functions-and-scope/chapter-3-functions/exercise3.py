# Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.

# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify_recursive(s):
    if len(s) == 70:
        print(s)
        return
    right_justify_recursive(' ' + s)

def right_justify_stringRepetition(s):
    print(' ' * (70-len(s)) + s)

# right_justify_recursive('nick')
right_justify_stringRepetition('nick')