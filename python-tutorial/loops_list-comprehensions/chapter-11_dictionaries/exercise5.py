# Exercise 11.5
# Think Python
# Chapter 11 - Dictionaries
# Exercise 5

# Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict.

"""
def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv
"""

# setdefault(key[,default]) - If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

from exercise2 import histogram

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]

        # for a key named 'val', set default equal to empty array if there is no key 'val' yet. in all cases, append key to the array
        inv.setdefault(val, []).append(key)

    return inv

print(invert_dict(histogram('mississippi')))