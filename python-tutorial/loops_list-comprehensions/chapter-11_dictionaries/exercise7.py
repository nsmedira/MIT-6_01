# Exercise 11.7
# Think Python
# Chapter 11 - Dictionaries
# Exercise 7

# Exponentiation of large integers is the basis of common algorithms for public-key encryption. 

# Read the Wikipedia page on the RSA algorithm3 and write functions to encode and decode messages.

import math

def encode(s):

    m = ''
    for c in s:

        # each character in the message is converted to a ascii decimal value
        m += str(ord(c))

    ##### TEST WIKIPEDIA EXAMPLE #####
    # m = 65

    # print('int m to encode:', m)

    return int(m)

def decode(i):
    # convert decrypted int back to string
    temp = str(i)
    decoded = ''
    while len(temp):
        if temp[:1] == '1':
            letter = chr(int(temp[:3]))
            temp = temp[3:]
        else:
            letter = chr(int(temp[0:2]))
            temp = temp[2:]
        decoded += letter
    
    return decoded

# requires an int m that is an int representation (in ascii) of our message
def generate_keys(m):

    # 1. Choose two distinct prime numbers p and q.

    ##### TEST WIKIPEDIA EXAMPLE #####
    # p, q = 61, 53

    # find two prime numbers whose product n will be greater than m
    i = math.ceil(math.sqrt(m))
    primes = []
    while len(primes) < 2:
        if isPrime(i):
            primes += [i]
        i += 1
    p, q = primes[0], primes[1]
    # print('p:', p)
    # print('q:', q)

    # 2. Compute n = pq.
    n = p * q
    in_range = int(m) < n
    if not in_range:
        print('m must be less than n')
        exit()

    # 3. Compute λ(n), where λ is Carmichael's totient function. Since n = pq, λ(n) = lcm(λ(p),λ(q)), and since p and q are prime, λ(p) = φ(p) = p − 1 and likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1).
    # The lcm may be calculated through the Euclidean algorithm, since lcm(a,b) = |ab|/gcd(a,b).
    a, b = (p - 1), (q - 1)
    lam = int(abs(a * b) / math.gcd(a, b))
    # print('lam:', lam)

    # 4. Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.

    ##### TEST WIKIPEDIA EXAMPLE #####
    # e = 17

    # accordng to wikipedia, the smallest (and fastest) possible value for e is 3: https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation
    i = 3

    while i < lam:
        if math.gcd(i, int(lam)) == 1:
            e = i
            break
        i += 1
    # print('e:', e)

    # 5. compute d where d * e ≡ 1 (mod lam)
    d = int(modInverse(e, lam))
    # print('d:', d)

    # print('public key [n, e]:', [n, e])
    # print('private key d:', d)

    return {'public': [n, e], 'private': d}

def encrypt_message(m, public):

    n, e = public[0], public[1]

    # generate ciphertext
    return pow(m, e, n)

def decrypt_message(cipher, n, d):

    # decrypt ciphertext
    return pow(cipher, d, n)

def RSA(s):
    m = encode(s)
    keys = generate_keys(m)
    cipher = encrypt_message(m, keys['public'])
    message = decrypt_message(cipher, keys['public'][0], keys['private'])

    messages_match = message == m
    if not messages_match:
        print('the decoded integer does not equal the encoded integer')
        exit()

    return decode(message)

# taken from https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

# modInverse(a, m) taken from https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 

if __name__ == "__main__":
    print(RSA('python')) # encrypts and decrypts message 'python'
    print(RSA('cat')) # encrypts and decrypts message 'cat'
    print(RSA('dog')) # encrypts and decrypts message 'dog'
    print(RSA('hello world')) # FAILS - encoded string does not equal decoded string