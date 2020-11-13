def zeroArray(m, n):

    # m lists with n zeroes
    t = []
    for _ in range(m):
        u = []
        for _ in range(n):
            u += [0]
        t += [u]

    return t

if __name__ == "__main__":
    print(zeroArray(4, 5))