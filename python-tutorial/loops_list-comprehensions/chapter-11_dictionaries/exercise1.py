# Exercise 11.1
# Think Python
# Chapter 11 - Dictionaries
# Exercise 1

# Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# If you did Exercise 10.8, you can compare the speed of this implementation with the list in operator and the bisection search.

import time

def create_dictionary(filepath):
    dictionary = dict()
    fin = open(filepath)
    for word in fin:
        word = word.strip('\n')
        dictionary[word] = ''

    return dictionary

def lookup(value, dictionary):
    start = time.time()
    is_in_dictionary = value in dictionary
    elapsed = time.time() - start
    print('dictionary searched in ', str(elapsed), 'seconds')
    print("'" + value + "' is in dictionary: " + str(is_in_dictionary))

dictionary = create_dictionary('../chapter-10_lists/words_lower.txt')
lookup('zookeepers', dictionary)

# performed a similar lookup function on the same word list in chapter-10_lists/exercise8.py 
# lookup('zookeepers', dictionary) took 2.1457672119140625e-06 seconds
# lookup('zookeepers', list) took 0.0008060932159423828 seconds