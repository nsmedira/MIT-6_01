# Testing float equality

Rather than checking whether x and y are exactly equal, it is safer to use the built-in function abs to compute the absolute value, or magnitude, of the difference between them:

```
if abs(y-x) < epsilon:
    break
```

Where `epsilon` has a value like 0.0000001 that determines how close is close enough.

# Algorithms

a mechanical process for solving a category of problems (in this case, computing square roots).