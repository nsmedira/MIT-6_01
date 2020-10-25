# Exercise 10.2
# Think Python
# Chapter 10 - Lists
# Exercise 2

# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

t = ['first', 'middle', 'last']

def chop(t):

    del t[0]
    del t[len(t)-1]

    return None

def middle(t):
    return t[1:len(t)-1]

# chop(t)
print(middle(t))
print(t)