# Exercise 12.5
# Think Python
# Chapter 12 - Tuples
# Exercise 5

# Here’s another Car Talk Puzzler:

# What is the longest English word, that remains a valid English word, as you remove its letters one at a time?

# Now, letters can be removed from either end, or the middle, but you can’t rearrange any of the letters. 
# Every time you drop a letter, you wind up with another English word. 
# If you do that, you’re eventually going to wind up with one letter and that too is going to be an English word—one that’s found in the dictionary. 
# I want to know what’s the longest word and how many letters does it have?

# I’m going to give you a little modest example: Sprite. Ok? 
# You start off with sprite, you take a letter off, one from the interior of the word, take the r away, and we’re left with the word spite, 
# then we take the e off the end, we’re left with spit, we take the s off, we’re left with pit, it, and I.

# Write a program to find all words that can be reduced in this way, and then find the longest one.

# This exercise is a little more challenging than most, so here are some suggestions:

# You might want to write a function that takes a word and computes a list of all the words that can be formed by removing one letter. These are the “children” of the word.

# Recursively, a word is reducible if any of its children are reducible. 
# As a base case, you can consider the empty string reducible.
# The wordlist I provided, words.txt, doesn’t contain single letter words. 
# So you might want to add “I”, “a”, and the empty string.
# To improve the performance of your program, you might want to memoize the words that are known to be reducible.

# You can see my solution at greenteapress.com/thinkpython/code/reducible.py.

def reducible_children(word, d):

    # word is reducible if it's already in our dictionary of reducible words
    if word in memo:
        m = memo[word]
        return m

    res = []

    # for each of the children of this word
    for child in children(word, d):

        # create a list of reducible children
        t = reducible_children(child, d)

        # if the list of reducible children has at least one child
        if t:

            # add the child to the result array
            res += [child]

    # if the result array as at least one word
    if res:

        # add the word as a key and the result array as a value to the memo dictionary
        memo[word] = res

    return res

def children(word, d):
    res = []
    for i in range(len(word)):

        # child is the parent word minus 1 letter
        child = word[:i] + word[i+1:]

        # if the child is in the dictionary
        if child in d:

            # add the child to the result array
            res += [child]

    return res

def build_dictionary(path):

    fin = open(path)

    d = dict()
    for word in fin:
        d.setdefault(word.strip('\n').lower(), '')

    # 'a', 'i', and '' need to be in the dictionary so they can be valid children
    for letter in ['a', 'i', '']:
        d[letter] = letter

    return d

memo = dict()
memo[''] = ['']

def find_reducibles(d):

    res = []

    # for every word in the dictionary
    for word in d:

        # get a list of reducible children
        t = reducible_children(word, d)

        # if the list contains at least 1 reducible child, add the word to the result array
        if t:
            res += [word]
    
    return res

def longest_word(d):

    # generate the total list of reducible words
    reducible_words = find_reducibles(d)

    t = []

    # for every reducible word
    for word in reducible_words:

        # add a tuple (length of the word, the word) to array t
        t += [(len(word), word)]

    # sort t descending
    t.sort(reverse=True)

    return t[0][1]

def print_trail(word):
    if len(word) == 0:
        return
    print(word)
    t = reducible_children(word, d)
    print_trail(t[0])

if __name__ == "__main__":

    # build the dictionary
    d = build_dictionary('../chapter-10_lists/words.txt')

    # find the longest word in the dictionary that can be reduced
    longest = longest_word(d)

    # show how the word can be reduced
    print_trail(longest)