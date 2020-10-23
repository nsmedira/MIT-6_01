def clip(lo, x, hi):

    # exception handling
    args = locals()
    for entry in args:
        if not isinstance(args[entry], int) and not isinstance(args[entry], float):
            return "each argument must be of type num"

    return min(max(lo, x), hi)