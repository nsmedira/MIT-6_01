def zeroVector(n):

    if not isinstance(n, int):
        return 'argument must be of type int'

    t = []
    for _ in range(n):
        t += [0]
    
    return t

if __name__ == "__main__":
    print(zeroVector(3))