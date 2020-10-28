# Exercise 11.2
# Think Python
# Chapter 11 - Dictionaries
# Exercise 2

# Dictionaries have a method called get that takes a key and a default value. If the key appears in the dictionary, get returns the corresponding value; otherwise it returns the default value. For example:

"""
>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0
"""

# Use get to write histogram more concisely. You should be able to eliminate the if statement.

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

if __name__ == "__main__":
    print(histogram('mississippi'))