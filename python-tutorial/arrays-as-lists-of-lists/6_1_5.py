def sumArray_1(a):
    
    return sum( [ sum(t) for t in a ] )

def sumArray_2(a):

    total = 0
    for t in a:
        for i in t:
            total += i

    return total

if __name__ == "__main__":
    print(sumArray_1([[1, 1, 1], [1, 1, 1]]))
    print(sumArray_2([[1, 1, 1], [1, 1, 1]]))