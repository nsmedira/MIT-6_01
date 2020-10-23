def mod(m, n):

    if (
        not isinstance (m, int)
        or not isinstance (n, int)
    ):
        return "both arguments have to be integers"

    if m <= 0 or n <= 0:
        return "both arguments have to be positive integers"

    # perform m mod n without using the modulo function

    # use a while loop to subtract n from m, keeping track of the remainder. exit while loop when remainder < m

    minuend = m
    while True:
        remainder = minuend - n 

        if remainder < n:
            break

        minuend = remainder

    return remainder