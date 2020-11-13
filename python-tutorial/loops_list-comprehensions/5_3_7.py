# Suppose we evaluate the following expressions: 

x={}
x['a']='apple'
x['b']='banana'
x['c']='chili dog' 

# Suppose we next evaluate more expressions, producing the 
# following sequence of interactions. Fill in each blank to 
# show what the Python interpreter would print at that point. 
# If an expression below would generate an error, enter error. 

x

x['c']
# value: 'chili dog'

x['banana']
# value: KeyError

x['a'] = 37
x['a']
# value: 37

# x.has_key('a')
# value: AttributeError: 'dict' object has no attribute 'has_key'