def piSeries(n):

    # approximate pi. see 5_3_8.pdf for equation

    # check type
    if not isinstance(n, int) or not n > 0:
        return "argument must be a positive integer"

    return sum( [ ((-1)**k) / ( 2*k + 1 ) for k in range(n) ] ) * 4

if __name__ == "__main__":
    print(piSeries(1000000))