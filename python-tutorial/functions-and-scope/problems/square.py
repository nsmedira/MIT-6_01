def square(x):

    # exception handling
    if not isinstance(x, int) and not isinstance(x, float):
        return "input must be a number"

    return x**2