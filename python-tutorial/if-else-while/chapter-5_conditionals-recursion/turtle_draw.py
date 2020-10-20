from swampy.TurtleWorld import *

def draw(t, length, n):

    if n == 0:
        return
    angle = 50

    # move turtle forward length*n
    fd(t, length*n)

    # turn turtle left 50 degrees
    lt(t, angle)

    # move forward a bit less and turn 50 degrees, recursively until n == 0
    draw(t, length, n-1)

    # turn turtle right 100 degrees
    rt(t, 2*angle)

    # move forward a bit less and turn 50 degrees, recursively until n == 0
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()
bob = Turtle()
draw(bob, 5, 4)

wait_for_user()