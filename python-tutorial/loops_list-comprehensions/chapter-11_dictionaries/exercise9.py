# Exercise 11.9
# Think Python
# Chapter 11 - Dictionaries
# Exercise 9

# Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 8.12).

# Write a program that reads a wordlist and finds all the rotate pairs.

def find_rotate_pairs(word_list):

    # create empty list of pairs [word, rotatedby, wordInDictionary]
    pairs = []
    
    # convert the word list into a dictionary
    words = dict()
    for word in word_list:
        words[word] = ''

    # for each word in the word list, rotate it 26 times and check to see if each rotation is in the dictionary
    for word in word_list:
        i = 1
        while i < 26:
            rotated = rotate_word(word, i)
            if rotated in words:
                pairs += [word, i, rotated]
            i += 1

    return pairs

def rotate_word(string, integer):

    string = string.lower()
    new = ''

    lower_bound = ord('a')
    upper_bound = ord('z')

    for letter in string:
        num = ord(letter)
        mod = abs(integer) % 26 # take remainder of abs(integer) / 26 since there are only 26 lower case letters
        if integer >= 0:
            c = num + mod 
        else:
            c = num - mod
        
        if c < lower_bound:
            c = upper_bound - (lower_bound - c) + 1
        elif c > upper_bound:
            c = lower_bound + (c - upper_bound) - 1

        new += chr(c)

    return new

if __name__ == "__main__":

    fin = open("../chapter-10_lists/words_lower.txt")

    word_list = []
    for word in fin:
        word_list += [word.strip('\n')]

    print(find_rotate_pairs(word_list))