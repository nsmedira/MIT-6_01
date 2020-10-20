from swampy.TurtleWorld import *

# To draw a Koch curve with length x, all you have to do is

# Draw a Koch curve with length x/3.
# Turn left 60 degrees.
# Draw a Koch curve with length x/3.
# Turn right 120 degrees.
# Draw a Koch curve with length x/3.
# Turn left 60 degrees.
# Draw a Koch curve with length x/3.

# The only exception is if x is less than 3. In that case, you can just draw a straight line with length x.

def koch(turtle, length):

    if length < 3:
        fd(turtle, length)
    else:

        third = length/3

        # step 1
        koch(turtle, third)

        # step 2
        lt(turtle, 60)

        # step 3
        koch(turtle, third)

        # step 4
        rt(turtle, 120)

        # step 5
        koch(turtle, third)

        # step 6
        lt(turtle, 60)

        # step 7
        koch(turtle, third)

def snowflake(turtle, function, length, n):

    while n > 0:
        function(turtle, length)
        rt(turtle, 120)
        n -= 1

world = TurtleWorld()
bob = Turtle()

snowflake(bob, koch, 100, 3)

wait_for_user()