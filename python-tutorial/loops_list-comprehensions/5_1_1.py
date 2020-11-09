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