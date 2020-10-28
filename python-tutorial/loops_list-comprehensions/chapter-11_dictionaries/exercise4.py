# Exercise 11.4
# Think Python
# Chapter 11 - Dictionaries
# Exercise 4

# Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none.

"""
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError
"""

def reverse_lookup(d, v):
    t = []
    for k in d:
        if d[k] == v:
            t += [k]
    return t

d = dict()
d['wrangler'] = 'suv'
d['tacoma'] = 'pickup'
d['fiesta'] = 'car'
d['civic'] = 'car'

e = dict()
e['banana'] = 'fruit'
e['apple'] = 'fruit'
e['orange'] = 'fruit'
e['strawberry'] = 'fruit'

print(reverse_lookup(e, 'fruit'))