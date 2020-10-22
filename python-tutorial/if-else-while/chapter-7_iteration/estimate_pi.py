import math

def estimate_pi():

    summation = 0
    k = 0

    while True:

        term = (factorial(4 * k) * (1103 + 26390 * k)) / (factorial(k)**4 * 396**(4 * k))

        summation += term

        if term < 1e-15:
            break
        
        k += 1

    return 1 / (((2 * math.sqrt(2))/9801)*summation)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(estimate_pi())
print(abs(math.pi - estimate_pi()))