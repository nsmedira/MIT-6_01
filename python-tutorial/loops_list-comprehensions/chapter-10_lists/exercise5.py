# Exercise 10.5
# Think Python
# Chapter 10 - Lists
# Exercise 5

# The (so-called) Birthday Paradox:

# 1. Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

# 2. If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.

from random import randint

t = [1, 2, 3]

def has_duplicates(t):
    for i in range(len(t)):
        if t[i] in t[i+1:]:
            return True
    return False

def class_has_two_same_birthdays(size):
    i = 0
    birthdays = []
    while i < size:
        birthday = randint(1, 365)

        # this was faster but i think the problem wants me to use the previously defined function has_duplicates

        # if birthday in birthdays:
        #     return True

        birthdays.append(birthday)
        if has_duplicates(birthdays):
            return True

        i += 1
    return False

def estimate_probability(i, size):
    count = 0
    j = 0
    while j < i:
        if class_has_two_same_birthdays(size):
            count += 1
        j += 1
    return 'the estimated probability is ' + str(count/i)

print(estimate_probability(100000, 23))