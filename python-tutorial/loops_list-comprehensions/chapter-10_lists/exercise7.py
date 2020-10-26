# Exercise 10.7
# Think Python
# Chapter 10 - Lists
# Exercise 7

# Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?

# You can see my [the author of Think Python] solution at greenteapress.com/thinkpython/code/wordlist.py.

# See word.txt in this directory for doc used

import time

def list_words_append():
    t = []
    fin = open('words.txt')
    for line in fin:
        for word in line.split():
            word = word.strip('.')
            if not word in t:
                t.append(word)
    return t

def list_words_add():
    t = []
    fin = open('words.txt')
    for line in fin:
        for word in line.split():
            word = word.strip('.')
            if not word in t:
                t = t + [word]
    return t

# print(list_words_append())
# print(list_words_add())
# print(list_words_add() == list_words_append())

start_time = time.time()
t = list_words_append()
elapsed_time = time.time() - start_time
print('append method:', str(elapsed_time))

start_time = time.time()
t = list_words_add()
elapsed_time = time.time() - start_time
print('addition of lists:', str(elapsed_time))

# addition is faster because it is adding a list to the original list object and assigning it to a new object

# append is slower because it is inserting an element into the end of the initial array, which inserts a reference to the new element resulting in infinite recursion

# https://stackoverflow.com/questions/2022031/python-append-vs-operator-on-lists-why-do-these-give-different-results