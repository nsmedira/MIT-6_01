# Exercise 11.10
# Think Python
# Chapter 11 - Dictionaries
# Exercise 10

# Here’s another Puzzler from Car Talk4:

# This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable, five-letter word recently that has the following unique property. 
# When you remove the first letter, the remaining letters form a homophone of the original word, that is a word that sounds exactly the same. 
# Replace the first letter, that is, put it back and remove the second letter and the result is yet another homophone of the original word. 
# And the question is, what’s the word?

# Now I’m going to give you an example that doesn’t work. 
# Let’s look at the five-letter word, ‘wrack.’ 
# W-R-A-C-K, you know like to ‘wrack with pain.’ 
# If I remove the first letter, I am left with a four-letter word, ’R-A-C-K.’ 
# As in, ‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’ 
# It’s a perfect homophone. 
# If you put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is a real word, it’s just not a homophone of the other two words.

# But there is, however, at least one word that Dan and we know of, which will yield two homophones 
# if you remove either of the first two letters to make two, new four-letter words. The question is, what’s the word?

# You can use the dictionary from Exercise 11.1 to check whether a string is in the word list.

# To check whether two words are homophones, you can use the CMU Pronouncing Dictionary. 
# You can download it from www.speech.cs.cmu.edu/cgi-bin/cmudict or from thinkpython.com/code/c06d.
# You can also download thinkpython.com/code/pronounce.py, which provides a function named read_dictionary that reads the pronouncing dictionary 
# and returns a Python dictionary that maps from each word to a string that describes its primary pronunciation.

# Write a program that lists all the words that solve the Puzzler. You can see my (Allen B Downey) solution at greenteapress.com/thinkpython/code/homophone.py.

from pronounce import read_dictionary

# check a word against the pronunciation dictionary
def check_word(word, dictionary):

    # see if both words (word minus second letter and word minus first letter) are in the pronunciation dictionary
    word1 = word[1:]
    word2 = word[0] + word[2:]
    if not word1 in dictionary or not word2 in dictionary:
        return False
    
    # both words are in the pronunciation dictionary. see if their pronunciations are equal
    return d[word1] == d[word2]

if __name__ == "__main__":

    # create python pronunciation dictionary
    d = read_dictionary()

    # create list of words
    word_list = []
    fin = open('../chapter-10_lists/words.txt')
    for word in fin:
        word_list += [word.strip('\n')]

    # check each word in the word list
    solves_puzzler = []
    for word in word_list:
        if check_word(word, d):
            solves_puzzler += [word]

    print ('words that solve puzzler:', solves_puzzler)