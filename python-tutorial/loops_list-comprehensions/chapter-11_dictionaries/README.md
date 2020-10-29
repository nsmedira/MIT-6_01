# Create a new dictionary

`dictionary = dict()` or `dictionary = {}`

# Add items to dictionary

`dictionary['electron'] = 'a stable subatomic particle with a charge of negative electricity, found in all atoms and acting as the primary carrier of electricity in solids'`

# Common function/methods/operations with dictionaries

`len()` returns the number of key-value pairs.

`in` operator compares a value to the *keys* in a dictionary

`values` method returns a list of values in the dictionary

`get(key, default)` returns the value of `key` or `default` if item can't be found

`keys` method returns a list of the keys in the dictionary

# Histogram

Statistical term for a set of counters

# For statement

With dictionaries, traverses the keys of a dictionary

# `raise`

Use `raise` to manually throw an exception e.g. `raise ValueError`. 

`raise` takes an error message as an optional argument e.g. `raise ValueError, 'value does not appear in the dictionary`

# Singleton

A list than contains a single element.

# Dictionary keys have to be hashable

Mutable types are not hashable (lists, dictionaries). Immutable types are (int, str)

## Hash

a function that takes a value (of any kind) and returns an integer. Dictionaries use these integers, called hash values, to store and look up key-value pairs.

# Global variables

 global variables (variables in `__main__`) can be accessed from any function. 
 
 Unlike local variables, which disappear when their function ends, global variables persist from one function call to the next.

 ## Flags

 It is common to use global variables for flags; that is, boolean variables that indicate (“flag”) whether a condition is true.

 ## Reassigning global variables inside a function

 Cannot directly reassign a global variable in a function (the variable will be interpreted as a new variable local to the function scope). To modify a global variable from within a function, declare it using the `global` statement:

 ```
 been_called = False

def example2():
    global been_called 
    been_called = True
```

## Mutating global variables inside a function

Mutable global varibles like lists or dictionaries can be called directly in a function without declaring them. But we must still declare a global mutable variable if we want to reassign it.

```
known = []
def example5():
    global known
    known = dict()
```

# Long integers

values of type `int` can range from -2147483648 through 2147483647

values of type `long` can be arbitrarily long

mathematical operators and functions in `math` module work on `long` as they don on `int`