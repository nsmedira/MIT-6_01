# Exercise 12.4
# Think Python
# Chapter 12 - Tuples
# Exercise 4

# More anagrams!

##### Part 1 #####

# Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.
# Here is an example of what the output might look like:

"""
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
"""

# Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled with those letters. 
# The question is, how can you represent the set of letters in a way that can be used as a key?

def find_anagrams(word_list):

    # create a dictionary to track the anagrams
    anagrams = dict()

    # build the dictionary
    for word in word_list:

        # create a list of the letters in this word
        t = list(word)
        
        # sort the list
        t.sort()
        
        # create a tuple from the sorted list
        t = tuple(t)

        # add this word to the dictionary
        anagrams.setdefault(t, []).append(word)

    # find dictionary keys with only 1 value
    one_value = []
    for key in anagrams:
        if len(anagrams[key]) <= 1:
            one_value += [key]

    # delete keys with one value from dictionary
    for key in one_value:
        del anagrams[key]

    return anagrams

if __name__ == "__main__":

    print('Part 1: Find the anagrams in a word list (printing first 10)\n')

    # open file
    fin = open('../chapter-10_lists/words.txt')

    # create word list
    word_list = []
    for word in fin:
        word_list += [word.strip('\n').lower()]

    result = find_anagrams(word_list)

    # print first 10 anagrams
    i = 0
    for key in result:
        print(result[key])
        i += 1
        if i >= 10:
            break

##### Part 2 #####

# Modify the previous program so that it prints the largest set of anagrams first, followed by the second largest set, and so on.

if __name__ == "__main__":

    print("\nPart 2: Print the sets of anagrams in descending order of length (printing first 10)\n")

    # empty list of tuples
    sorted_anagrams = []

    # iterate the dictionary and create the list of tuples (number of anagrams, key)
    for key in result:
        sorted_anagrams += [(len(result[key]), key)]

    # sort the list
    sorted_anagrams.sort(reverse=True)

    # print first 10 anagrams
    i = 0
    for t in sorted_anagrams:
        print(str(t[0]) + ':', result[t[1]])
        i += 1
        if i >= 10:
            break

##### Part 3 #####

# In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. 
# What set of 8 letters forms the most possible bingos? 
# Hint: there are seven.

if __name__ == "__main__":
    
    print('\nPart 3: find the set of 8 letters that form the greatest possible scrabble bingos (7)\n')

    # empty list of tuples
    sorted_anagrams = []

    # iterate the dictionary and create list of tuples (length of key, number of anagrams, key)
    for key in result:
        length = len(key)
        if length == 8:
            sorted_anagrams += [(length, len(result[key]), key)]

    # sort the list
    sorted_anagrams.sort(reverse=True)

    # what is the greatest number of anagrams?
    maxi = sorted_anagrams[0][1]

    # print out the set of 8 letters where the number of anagrams == maxi
    for t in sorted_anagrams:
        if t[1] == maxi:
            print(str(t[2]) + ':', result[t[2]])

##### Part 4 #####

# Two words form a “metathesis pair” if you can transform one into the other by swapping two letters.
# For example, “converse” and “conserve.” Write a program that finds all of the metathesis pairs in the dictionary. 
# Hint: don’t test all pairs of words, and don’t test all possible swaps.

if __name__ == "__main__":

    print('\nPart 4: find metathesis pairs (print first 10)\n')

    metathesis_pairs = []

    # a metathesis pair must also be anagrams, so we can iterate over the dictionary of anagrams
    for key in result:

        t = result[key]

        list_length = len(t)

        key_length = len(key)

        # compare each word in the list to the remaining words in the list
        for i in range(list_length):
            j = i + 1
            while j < list_length:

                k = 0

                # two words in a list of anagrams will be metathesis pairs if all but two of their indexes are equal
                num_mismatched = 0

                # for two words in a list, compare the values at a given index and keep track of how many mismatch
                while k < key_length:
                    if t[i][k] != t[j][k]:
                        num_mismatched += 1
                    k += 1
                
                # if two indexes were mismatched, it is a metathesis pair
                if num_mismatched == 2:
                    metathesis_pairs += [[t[i], t[j]]]

                j += 1

    print(metathesis_pairs[:10])

# You can download a solution from greenteapress.com/thinkpython/code/anagram_sets.py.