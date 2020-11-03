# Tuples are immutable

Tuples are like lists in that they are a sequence of values indexed by integer. Unliked lists, however, they are immutable.

# Comma separated list of values

`t = 'a', 'b', 'c'`

It is not necessary but tuples can be enclosed in parentheses.

`t = ('a', 'b', 'c')`

# Tuple with a single element

Have to include a final comma.

`t = 'a',`

# tuple() function

`t = tuple()`

## if argument is a sequence

result is a tuple with the elements of the sequence:

```
>>> t = tuple('lupins')
>>> print t
('l', 'u', 'p', 'i', 'n', 's')
```

# Operators

Most list operators also work on tuples. For example, the bracket and slice operators.

# Immutable. 

You can't modify the elements of a tuple but you can replace a tuple with another tuple.

# Tuple assignment

`>>> a, b = b, a`

The left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments.

the right side can be any kind of sequence (string, list or tuple). For example, to split an email address into a user name and a domain, you could write:

```
>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
```

# Variable-length argument tuples

## Gather

A parameter name that begins with * gathers arguments into a tuple. For example, printall takes any number of arguments and prints them:

```
def printall(*args):
    print args
```

## Scatter

If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the * operator. For example, divmod takes exactly two arguments; it doesn’t work with a tuple:

```
>>> divmod(*t)
(2, 1)
```

# zip()

built-in function that takes two or more sequences and “zips” them into a list of tuples where each tuple contains one element from each sequence

```
>>> s = 'abc'
>>> t = [0, 1, 2]
>>> zip(s, t)
[('a', 0), ('b', 1), ('c', 2)]
```

If the sequences are not the same length, the result has the length of the shorter one.

```
>>> zip('Anne', 'Elk')
[('A', 'E'), ('n', 'l'), ('n', 'k')]
```

# tuples and lists

You can use tuple assignment in a for loop to traverse a list of tuples:

```
t = [('a', 0), ('b', 1), ('c', 2)] 
for letter, number in t:
    print number, letter
```

If you need to traverse the elements of a sequence and their indices, you can use the built-in function enumerate:

```
for index, element in enumerate('abc'): 
    print index, element
```

# Dictionaries and tuples

Dictionaries have a method called items that returns a list of tuples, where each tuple is a key-value pair

```
>>> d = {'a':0, 'b':1, 'c':2} 
>>> t = d.items()
>>> print t
[('a', 0), ('c', 2), ('b', 1)]
```

Conversely, you can use a list of tuples to initialize a new dictionary:

```
>>> t = [('a', 0), ('c', 2), ('b', 1)] 
>>> d = dict(t)
>>> print d
{'a': 0, 'c': 2, 'b': 1}
```

It is common to use tuples as keys in dictionaries (primarily because you can’t use lists). For example, a telephone directory might map from last-name, first-name pairs to telephone numbers.

# Comparing tuples

Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next elements, and so on, until it finds elements that differ.

The `sort` function works the same way. It sorts primarily by first element, but in the case of a tie, it sorts by second element, and so on.


## Decorate Sort Undecorate (DSU) pattern

**Decorate** a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence

**Sort** the list of tuples

**Undecorate** by extracting the sorted elements of the sequence

# Why use one sequence over another?

We have strings, lists and tuples. Strings have to be made up or characters. Lists are common because they are mutable.

Reasons why you might prefer tuples:
1. In some contexts, like a `return` statement, it is syntactically simpler to create a tuple than a list. In other contexts, you might prefer a list.
2. If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.
3. If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.