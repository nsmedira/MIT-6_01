# For each of the expressions below, specify its type and value. 
# If it generates an error, select type noneType 
# and put the word error in the box for the value. 
# Assume we've made the following assignments: 

a = 'hi'
x = [1,2,[3,'John',4],'Hi'] 

# 1
a
# type = string
# value = 'hi'

# 2
a[0]
# type = string
# value = 'h'

# 3
a[1]
# type = string
# value = 'i'

# 4
a[2]
# type = NoneType
# value = IndexError: string index out of range

# 5
x[0]
# type = int
# value = 1

# 6
x[2]
# type = list
# value = [3, 'John', 4]

# 7
x[-1]
# type = string
# value = 'Hi'

# 8
x[2][2]
# type = int
# value = 4

# 9
x[2][-1]
# type = int
# value = 4

# 10
x[-1][2]
# type = noneType
# value = IndexError: string index out of range

# 11
x[0:1]
# type = list
# value = [1]

# 12
x[0:-1]
# type = list
# value = [1, 2, [3, 'John', 4]]

# 13
len(x)
# type = int
# value = 4

# 14
(a, b, c, d) = x
c
# type = list
# value = [3, 'John', 4]

# 15
range(3)
# type = range
# value = range(0, 3)

# 16
range(3, 10)
# type = range
# value = range(3, 10)

# 17
range(3, 10, 3)
# type = range
# value = range(3, 10, 3)

# 18
range(10, 3)
# type = range
# value = range(10, 3)

# 19
range(10, 3, -1)
# type = range
# value = range(10, 3, -1)

# 20
range(len(x))
# type = range
# value = range(0, 4)

# 21
'hi' == 'Hi'
# type = bool
# value = False

# 22
2 in x
# type = bool
# value = True

# 23
3 in x
# type = bool
# value = False

# 24
'John' in x
# type = bool
# value = False

# 25
'Hi' in x
# type = bool
# value = True

# 26
sum(range(4))
# type = int
# value = 6

# 27
[x for x in range(3)]
# type = list
# value = [0, 1, 2]

# 28
[x*2 for x in range(3)]
# type = list
# value = [0, 2, 4]

# 29
sum([x*2 for x in range(3)])
# type = int
# value = 6

# 30
[-x for x in [8, 2, 1]]
# type = List
# value = [-8, -2, -1]

# 31
def fizz(x): return x + 1
[fizz(fizz(x)) for x in [8, 2, 1]]
# type = list
# value = [10, 4, 3]

# 32
[x for x in range(10) if x%2 == 0]
# type = list
# value = [0, 2, 4, 6, 8]