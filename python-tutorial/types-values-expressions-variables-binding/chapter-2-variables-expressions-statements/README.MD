# [Chapter 2: Variables, expressions and statements](http://www.greenteapress.com/thinkpython/html/book003.html)

# Keywords

- and
- as
- assert
- break
- class
- continue
- def
- del
- elif
- else
- except
- ~~exec~~ (removed in Python3)
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- **nonlocal** (added in Python3)
- not
- or
- pass
- print
- raise
- return
- try
- while
- with
- yield

# 2.5 Operators and operands

Python uses `**` for exponentiation e.g. `5**2`

With two integers, Python performs floor division, chopping off any remainder and returning an integer

E.g. `59/60` = 0

# 2.7 Order of operations

PEMDAS

1. Parentheses
2. Exponentiation
3. Multiplication and Division
4. Addition and Subtraction

Operators with the same precedence are evaluated from left to right (except exponentiation)

# 2.8 String operations

A string can be multiplied by a integer to produce repetition

`'spam' * 3` = 'spamspamspam'

# Exercise 4

Create timedelta objects to compute difference in two times

```
from datetime import timedelta

t1 = timedelta(hours=6, minutes=62)
t2 = timedelta(seconds=totalSeconds)
newTime = t1 + t2
```
