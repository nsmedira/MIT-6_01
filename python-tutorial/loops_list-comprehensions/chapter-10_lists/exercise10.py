# Exercise 10.10
# Think Python
# Chapter 10 - Lists
# Exercise 10

# Two words “interlock” if taking alternating letters from each forms a new word1. For example, “shoe” and “cold” interlock to form “schooled.”

# 1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!

# 2. Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?

from custom_bisect import bisect
import time

def find_interlocking_words(t, num):

    start = time.time()

    # accept a sorted list of words and a number that represents how many interlocking "words" make it up

    # create a list to store arrays of interlocking words
    interlocking_words = []
    
    # go through each word and see separate it into num words
    for i in range(len(t)):

        # if i % 1000 == 0:
        #     print('i:', i)
        #     print('interlocking_words so far:', interlocking_words)
        #     print('elapsed time:', str(time.time() - start))

        subs = []

        # use extended slices (optional third argument in the slicing syntax: 'step' or 'stride')
        for j in range(num):
            subs += [t[i][j::num]]

        interlock = True
        for w in subs:
            if bisect(t, w) == None:
                interlock = False
                break

        if interlock == True:
            interlocking_words += [subs]

    print('elapsed time:', str(time.time() - start))

    return interlocking_words
            
fin = open('words_lower.txt')

word_list = []

for word in fin:
    word_list += [word.strip('\n').lower()]

# print(find_interlocking_words(['cold', 'schooled', 'shoe'], 2))
print(find_interlocking_words(sorted(word_list), 5))