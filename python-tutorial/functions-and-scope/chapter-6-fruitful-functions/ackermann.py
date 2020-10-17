def a (m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return a(m-1, 1)
    elif m > 0 and n > 0:
        return a(m-1, a(m, n-1))

print(a(3,4))

# what happens for larger values of m and n?
# lots of recursion?