# Exercise 10.8
# Think Python
# Chapter 10 - Lists
# Exercise 8

# To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.

# Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary. You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you search the second half.

# Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there.

# Write a function called bisect that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.

# Or you could read the documentation of the bisect module and use that!

import math
import time
from custom_bisect import bisect

fin = open('words_lower.txt')
word_list = []
for word in fin:
    word_list = word_list + [word.strip('\n')]

# print(len(word_list))
def lookup(value, t):
    start = time.time()
    is_in_list = value in t
    elapsed = time.time() - start
    print('list searched in ', str(elapsed), 'seconds')
    print("'" + value + "' is in list: " + str(is_in_list))

lookup('zookeepers', word_list)

# word_list[0]
print(bisect(word_list, 'aardvark')) 

# word_list[1]
print(bisect(word_list, 'aardwolf')) 

# word_list[2]
print(bisect(word_list, 'aaron')) 

# word_list[3]
print(bisect(word_list, 'aback')) 

# word_list[4]
print(bisect(word_list, 'abacus')) 

# word_list[5]
print(bisect(word_list, 'abaft')) 

# word_list[18779]
print(bisect(word_list, 'fantods')) 

# word_list[58110]
print(bisect(word_list, 'zulus')) 

# None
print(bisect(word_list, 'asdlkjaslkdjfalksjdf')) 