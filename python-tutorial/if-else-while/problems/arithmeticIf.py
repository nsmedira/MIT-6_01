def arithmeticIf(v, a, b, c):

    if not isinstance(v, int) and not isinstance(v, float):
        return "v must be of type num"

    if v > 0:
        return a
    elif v == 0:
        return b
    elif v < 0:
        return c