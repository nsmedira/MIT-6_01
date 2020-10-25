# Lists are mutable

Bracket operator can appear on the left side of an assignment:

`numbers[1] = 5`

# Indices

List indices work the same way as string indices:

- negative index counts backwards from the end of the list

# `in` operator also works on list

# `range`

`range(n)` returns a list of indices from 0 to *n*-1 where *n* is the length of the list

# List operations

The `+` operator concatenates lists

The `*` operator repeats a list

# List slices

A slice operator on the left side of an assignment can update multiple elements:


```
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print t
['a', 'x', 'y', 'd', 'e', 'f']
```

# List methods

`append` adds a new element to the end of a list

`extend` takes a list as an argument and appends all of the elements

`sort` arranges the elements of a list from low to high

List methods are all void

# Map, filter, reduce

`sum(list)` 

```
>>> t = [1, 2, 3]
>>> sum(t)
6
```

**reduce** - An operation that combines a sequence of elements into a single value

**map** - "maps" a function onto each of the elements in a sequence

**filter** - selects some of the elements and filters out the others

# Deleting elements

`pop` method modifies the list and returns the element that was removed. If you don’t provide an index, it deletes and returns the last element.

```
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print t
['a', 'c']
>>> print x
b
```

If you don’t need the removed value, you can use the `del` operator:

```
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print t
['a', 'c']
```

To remove more than one element, you can use `del` with a slice index:

```
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> print t
['a', 'f']
```

If you know the element you want to remove (but not the index), you can use `remove`. The return value from remove is None.

```
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print t
['a', 'c']
```

# Lists and strings

To convert from a string to a list of characters, you can use `list`:

```
>>> s = 'spam'
>>> t = list(s)
>>> print t
['s', 'p', 'a', 'm']
```

If you want to break a string into words, you can use the `split` method:

```
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print t
['pining', 'for', 'the', 'fjords']
```

`split` takes optional delimiter value.

```
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
```

`join` is the inverse of `split`. It takes a list of strings and concatenates the elements. `join` is a string method, so you have to invoke it on the delimiter and pass the list as a parameter:

```
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```

# Objects and values

To check whether two variables refer to the same object, you can use the `is` operator.

Two variables equal to the same string both reference the same string object.

Two equivalent lists reference separate list objects (the two lists are **equivalent**, because they have the same elements, but not **identical**, because they are not the same object)

# Aliasing

An object with more than one reference has more than one name, so we say that the object is **aliased**.

If the aliased object is mutable, changes made with one alias affect the other.

# List arguments

When you pass a list to a function, the function gets a reference to the list. If the function modifies a list parameter, the caller sees the change.