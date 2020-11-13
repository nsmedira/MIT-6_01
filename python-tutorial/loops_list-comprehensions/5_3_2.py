def everyOther(t):

    # write a procedure that takes a list as input
    # and returns a new list with alternating elements of the origina list
    # starting with the first

    return [t[i] for i in range(0, len(t), 2)]

if __name__ == "__main__":
    print(everyOther([1, 2, 3, 4, 5]))