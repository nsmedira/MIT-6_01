# Exercise 10.6
# Think Python
# Chapter 10 - Lists
# Exercise 6

# Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original. Hint: they don’t have to be in the same order.

def remove_duplicates(t):
    new = []
    for i in t:
        if not i in new:
            new.append(i)
    return new

print(remove_duplicates([1, 2, 2, 3]))