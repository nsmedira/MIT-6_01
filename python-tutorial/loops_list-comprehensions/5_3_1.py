def multIA(m, n):

    # return product of m and n
    # assuming n is a positive integer
    # don't use *
    # instead, use a for loop and +
    # even though we first asked you to do this with while,
    # generally speaking, any iteration over a fixed set of values
    # is clearer and easier to write as a for loop
    # your function should have type (num, positiveInt) -> num

    # check input typing
    number_types = (int, float, complex)
    if (
        not isinstance(m, number_types) 
        or not isinstance(n, int)
        or not n > 0
    ):
        return 'arguments must have type (num, positiveInt)'

    product = 0
    for _ in range(n):
        product += m
    
    return product

if __name__ == "__main__":
    print(multIA(0, 5))