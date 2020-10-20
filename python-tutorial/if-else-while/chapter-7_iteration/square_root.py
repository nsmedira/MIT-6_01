def square_root(a):

    x = a / 2

    epsilon = .0000001

    while True:
        print (x)
        y = (x + a/x) / 2

        # don't compare x and y directly, rather test if the absolute value of the difference between them is less than an exceptable margin of error epsilon
        # if y == x:
        if abs(y-x) < epsilon:
            break
        x = y

square_root(1000)