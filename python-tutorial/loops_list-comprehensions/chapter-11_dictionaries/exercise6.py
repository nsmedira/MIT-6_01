# Exercise 11.6
# Think Python
# Chapter 11 - Dictionaries
# Exercise 6

# fully recursive fibonacci(n) implementation
"""
def fibonacci (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

# fibonacci(n) implemented with a memo that tracks our known fibonacci values
"""
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
"""

# Run this version of fibonacci (the one with a memo implementation) and the original with a range of parameters and compare their run times.

import time

def fibonacci (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

known = {0:0, 1:1}

def fibonacci_memo(n):

    if n in known:
        return known[n]

    res = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    known[n] = res
    return res

def compare_fibs(n):

    start_fib = time.time()
    res = fibonacci(n)
    elapsed_fib = time.time() - start_fib

    start_fib_memo = time.time()
    res_memo = fibonacci_memo(n)
    elapsed_fib_memo = time.time() - start_fib_memo

    print("n:", n)
    print("fibonacci")
    print("result:", res)
    print("elapsed time:", elapsed_fib)
    print()
    print("fibonacci_memo")
    print("result:", res_memo)
    print("elapsed time:", elapsed_fib_memo)
    print()

compare_fibs(25)
compare_fibs(30)
compare_fibs(35)
compare_fibs(40)
compare_fibs(45)
compare_fibs(50)