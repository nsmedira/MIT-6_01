# Exercise 10.9
# Think Python
# Chapter 10 - Lists
# Exercise 9

# Two words are a “reverse pair” if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list.

from custom_bisect import bisect

def find_reverse_pairs(t):

    # create empty list of reverse pairs
    reverse_pairs = []
    index_is_reverse_pair = []   
    
    for i in range(len(t)):

        # if the word is already in the array of reverse pairs, continue
        if len(index_is_reverse_pair) > 0 and bisect(sorted(index_is_reverse_pair), i) != None:
            continue

        # define the reverse of a word
        reverse = ''
        word = t[i]

        # print(word)

        j = len(word) - 1
        while j >= 0:
            reverse += word[j]
            j -= 1
            
        # print(reverse)

        # now that we have the reverse of the word, look for it in the list
        result = bisect(t, reverse)

        # print(result)

        if result != None and result != i:
            reverse_pairs += [[word, reverse]]
            index_is_reverse_pair += [i, result]
    
    return reverse_pairs

fin = open('words_lower.txt')
word_list = []
for word in fin:
    word_list += [word.strip('\n')]

print(find_reverse_pairs(sorted(word_list)))