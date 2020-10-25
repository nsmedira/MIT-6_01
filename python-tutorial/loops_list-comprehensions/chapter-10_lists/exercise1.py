# Exercise 10.1
# Think Python
# Chapter 10 - Lists
# Exercise 1

# Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

def cumulative_sum(l):
    res = []
    for i in range(len(l)):
        if i == 0:
            res.append(l[i])
        else:
            res.append(l[i] + res[i-1])
    return res

print(cumulative_sum([1,2,3]))