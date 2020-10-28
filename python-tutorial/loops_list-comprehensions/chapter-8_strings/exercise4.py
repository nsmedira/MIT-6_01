# Exercise 8.4
# Think Python
# Chapter 8 - Strings
# Exercise 4

# Modify find so that it has a third parameter, the index in word where it should start looking.

def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# print(find('apple', 'a', 1))