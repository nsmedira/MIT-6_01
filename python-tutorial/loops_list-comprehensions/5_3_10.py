from piSeries import piSeries
import math

def numTerms_loop(eps):

    # check type
    if not isinstance(eps, float):
        return 'argument must be of type float'

    n = 0
    pi = math.pi
    while True:
        n += 1
        if within(piSeries(n), pi, eps):
            return n

# can't quite figure out how to improve performance
"""
def numTerms(eps):

    # check type
    if not isinstance(eps, float):
        return 'argument must be of type float'

    n = int(1 // eps)
    pi = math.pi
    while True:
        if within(piSeries(n), pi, eps):
            return n
        n += 1
"""

def within(x, y, eps):
    return abs(x - y) < eps

if __name__ == "__main__":
    print(numTerms_loop(.001))