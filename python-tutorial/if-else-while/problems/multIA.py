def multIA(m, n):
    if (
        not isinstance(m, int) and not isinstance(m, float)
        or not isinstance(n, int) or n <= 0
    ):
        return "arguments must be of type (num, positiveInt)"

    # each iteration through the loop, add m to the sum. end after n iterations through the loop
    product = 0
    i = 0
    while i < n:
        product += m
        i += 1

    return product