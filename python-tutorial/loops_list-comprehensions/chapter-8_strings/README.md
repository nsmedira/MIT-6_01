# String is a sequence

Can access the characters of a string with the bracket operator.

# Negative indices

`string[-1]` yields last letter in `string`. `string[-2]` yields second to last letter in `string`

# Slices

Select a slice of a string with `[n:m]` operator. The slice will include the nth index but not the mth

Omitting the nth index starts from the beginning of the string.

Omitting the mth index goes to the end of the string.

Omitting the nth and mth index e.g. `[:]` returns the entire string.

If first index is greater than or equal to the second, the result is an empty string.

A string slice can take a third index that specifies the “step size;” that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

```
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
```

A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.

# Strings are immutable

# Search

Traversing a sequence and returning when we find what we are looking for.

# Function vs Method Syntax

Function *call*: `upper(word)`

Method *invocation*: `word.upper()`

# `Find` method for string objects

Can find index where single characters or substrings occur: `word.find('a')` or `word.find('na')`

Can take a second argument specifying where the search should start. 

Can take a third index specifying where it should stop (does not include end index).

# `in` operator

boolean operator that takes two strings and returns True if the first appears as a substring in the second

# String comparison

If `word1 == word2` they are the same word.

If `word1 < word2`, `word1` comes before `word2`

If `word1 > word2`, `word1` comes after `word2`

Uppercase letters always come before lowercase letters. 

# String method documentation

[https://docs.python.org/2.5/lib/string-methods.html](https://docs.python.org/2.5/lib/string-methods.html)

## `replace(old, new[, count])`

Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

## `strip([chars])`

Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:

```
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
```