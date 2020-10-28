# MIT-6_01 - Introduction to EECS 1 from MIT OCW

# Run Python programs

In shell, `python3 <filename>`

# Exit Python interpreter

`exit()`

# [`__main__` - Top-Level Script Environment](https://docs.python.org/3/library/__main__.html)

`__main__` is the name of the scope in which top-level code executes. A module’s `__name__` is set equal to `__main__` when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the main scope by checking its own `__name__`, which allows a common idiom for conditionally executing code in a module when it is run as a script or with `python -m` but not when it is imported:

```
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

For a package, the same effect can be achieved by including a `__main__.py` module, the contents of which will be executed when the module is run with `-m`.