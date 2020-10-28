# Exercise 11.3
# Think Python
# Chapter 11 - Dictionaries
# Exercise 3

# Dictionaries have a method called keys that returns the keys of the dictionary, in no particular order, as a list.

# Modify print_hist to print the keys and their values in alphabetical order.

"""
def print_hist(h):
    for c in h:
        print c, h[c]
"""

from exercise2 import histogram

def print_hist(h):
    t = sorted(h.keys())
    for i in t:
        print(i, ": ", h[i])

if __name__ == "__main__":
    print_hist(histogram('mississippi'))