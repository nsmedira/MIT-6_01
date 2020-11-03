# Exercise 12.2
# Think Python
# Chapter 12 - Tuples
# Exercise 2

# In this example, ties are broken by comparing words, so words with the same length appear in reverse alphabetical order. 
# For other applications you might want to break ties at random. 
# Modify this example so that words with the same length appear in random order. 

"""
def sort_by_length(words): 
    t = []
    for word in words: 
        t.append((len(word), word))
        
    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word) 
        return res
"""

# Hint: see the random function in the random module.

from random import random
import math

def sort_by_length(words): 

    # assign a random number between 1 and the length of the word list in the oneth index of each tuple
    length = len(words)

    t = []
    for word in words: 
        t.append((len(word), math.floor(random() * length) + 1, word))
        
    t.sort(reverse=True)

    print(t)
    exit()

    res = []
    for length, word in t:
        res.append(word) 
        return res

if __name__ == "__main__":
    sort_by_length(['house', 'pods', 'knob', 'car', 'she', 'he'])