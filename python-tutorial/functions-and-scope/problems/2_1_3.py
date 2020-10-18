# scoping

# 1. value = 7
def foo (x):
    def bar (x):
        return x + 1
    return bar (x * 2)
print(foo(3))

# 2. value = 5
def foo_2 (x):
    def bar (z):
        return z + x
    return bar(3)
print(foo_2(2))