def div(m, n):

    if (
        not isinstance(m, int) and m <= 0
        or not isinstance(n, int) and n <= 0
    ):
        return "both arguments have to be positive integers"
    
    minuend = m
    times = 0
    while True:
        remainder = minuend - n 

        if remainder >= 0:
            times += 1
        else:
            break

        minuend = remainder

    return times