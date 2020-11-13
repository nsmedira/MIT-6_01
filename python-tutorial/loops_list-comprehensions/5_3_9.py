def evalPolynomial(coeffs, x):

    num_types = (int, float, complex)
    if not isinstance(coeffs, list) or not isinstance(x, num_types):
        return 'arguments must be (list, num)'

    for i in coeffs:
        if not isinstance(i, int):
            return 'each element in the list must be an integer'

    coeffs = sorted(coeffs, reverse=True)

    length = len(coeffs)

    return sum( [ coeffs[i] * x ** ( length - i - 1 ) for i in range(length) ] )


if __name__ == "__main__":
    print(evalPolynomial([1, 2, 3, 4], 2))