from multIA import multIA

def multIAgen(m, n):

    # both inputs have to be int
    if (
        not isinstance(m, int) 
        or not isinstance(n, int)
    ):
        return "both inputs have to be type int"

    if m == 0 or n == 0:
        return 0
    
    # either input can be negative. determine sign of product
    if n < 0 and m < 0:
        m = abs(m)
    return multIA(m, abs(n))

print(multIAgen(0, 0))