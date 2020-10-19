# Modulus Operator

you can extract the right-most digit or digits from a number. For example, x % 10 yields the right-most digit of x (in base 10). Similarly x % 100 yields the last two digits.

# Relational Operators

x == y               # x is equal to y
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y

Remember that = is an assignment operator and == is a relational operator.

# Logical Operators

and, or, and not

the operands of the logical operators should be boolean expressions

Any nonzero number is interpreted as “true.”

# Pass

Occasionally, it is useful to have a body with no statements (usually as a place keeper for code you haven’t written yet). In that case, you can use the pass statement, which does nothing.

```
if x < 0:
    pass
```

# Base Case

does not make a recursive call

# Keyboard Input

`input()` gets input from the keyboard, returns that input as a string

# Error messages (tracebacks)

In general, error messages tell you where the problem was discovered, but that is often not where it was caused.