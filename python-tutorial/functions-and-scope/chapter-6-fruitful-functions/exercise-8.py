# The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

# One way to find the GCD of two numbers is Euclid’s algorithm, which is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can consider gcd(a, 0) = a.


# Write a function called gcd that takes parameters a and b and returns their greatest common divisor. If you need help, see wikipedia.org/wiki/Euclidean_algorithm.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    print(gcd(1000000,1001000))