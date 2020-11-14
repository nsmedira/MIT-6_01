# the big ideas

- Primitives lead to combinations via composition.
- If a particular kind of combination is seen frequently, it can be identified as a
pattern.
- If we want to interact with the pattern, and not the primitives or combination, we
create an abstraction. A procedure is a good example of such an abstraction.
- Environments: Look in the most local scope for a binding of a given variable. If
found, return the binding. If not, check the parent scope. Repeat until you find an
assignment, or reach the global scope.
- Classes and Instances are Environments
- `pat.salutation()` is exactly equivalent to `Staff601.salutation(pat)` (see
Chapter 2 of the Course Notes) 

# vocabulary

- [interpreter vs. compiler](https://www.businessinsider.in/difference-between-compiler-and-interpreter/articleshow/69523408.cms)
- expression - a syntactic entity in a programming language that may be evaluated to determine its value. It is a combination of one or more constants, variables, functions, and operators that the programming language interprets and computes to produce another value

