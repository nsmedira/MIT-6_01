# Exercise 11.8
# Think Python
# Chapter 11 - Dictionaries
# Exercise 8

# If you did Exercise 10.5, you already have a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

"""
def has_duplicates(t):
    for i in range(len(t)):
        if t[i] in t[i+1:]:
            return True
    return False
"""

# Use a dictionary to write a faster, simpler version of has_duplicates.
# referenced https://epequeno.wordpress.com/2011/11/23/exercise-11-8/ for tip on the get() method


def has_duplicates(t):

    freq = dict()
    for i in range(len(t)):
        freq[t[i]] = 1 + freq.get(t[i], 0)
        if freq[t[i]] > 1:
            return True
    return False

if __name__ == "__main__":
    print(has_duplicates(['a', 'b', 'c', 'a']))