# Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks with the given lengths.

# If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can

import fermat_2

def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print('no')
    else:
        print('yes')

def is_triangle_from_inputs():
    user_inputs = fermat_2.collect_inputs(['a', 'b', 'c'])
    if user_inputs == 'q':
        print("quitting program...")
        return
    is_triangle(user_inputs[0], user_inputs[1], user_inputs[2])

is_triangle_from_inputs()