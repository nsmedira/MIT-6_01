# lambda

```
>>> g = lambda x,y : x * y
>>> g(3, 4)
12 
```

# defining functions inside other functions

if we don't expect to use them elsewhere

# List comprehensions

`[expr for var in list]`

where `var` is a single variable, `list` is an expression that results in a list, and `expr` is an
expression that uses the variable `var`. The result is a list, of the same length as `list`,
which is obtained by successively letting `var` take values from `list`, and then evaluating
`expr`, and collecting the results into a list. 

```
>>> [x/2.0 for x in [4, 5, 6]]
[2.0, 2.5, 3.0]
>>> [y**2 + 3 for y in [1, 10, 1000]]
[4, 103, 1000003]
>>> [a[0] for a in 
```

## filtering

```
>>> nums = [1, 2, 5, 6, 88, 99, 101, 10000, 100, 37, 101]
>>> [x for x in nums if x%2==1]
[1, 5, 99, 101, 37, 101]
```