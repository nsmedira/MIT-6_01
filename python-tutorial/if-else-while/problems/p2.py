def p2(x):

    if not isinstance(x, int):
        return "argument must be an integer"

    if x > 1:

        # start exp at 1 because 2 ** 0 = 1 and that will never be greater than x in this if clause
        exp = 1

        # start power at 1 because 2 ** 0 = 1 and that is the largest power of 2 that could be less than any value of x in this if clause
        power = 1
        while True:
            temp = 2 ** exp
            if temp >= x:
                return power
            power = temp
            exp += 1

    else:
        return 0