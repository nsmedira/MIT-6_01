# Exercise 10.4
# Think Python
# Chapter 10 - Lists
# Exercise 4

# Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(str1, str2):
    
    # convert strings to lower case
    str1 = str1.lower()
    str2 = str2.lower()

    # convert strings to lists
    t1 = list(str1)
    t2 = list(str2)

    # compare sorted lists
    return sorted(t1) == sorted(t2)

print(is_anagram('listen', 'silent'))