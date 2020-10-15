# Part 1
# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.

# print '+', 
# print '-'
# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

def drawGrid(cols, rows):

    # if 0 columns or 0 rows simply return
    if cols == 0 or rows == 0:
        print('at least one row and one column required')
        return

    # draw the top beams
    printBeams(cols)

    # print a row of the grid
    count = 0
    while count < rows:
        printRow(cols)
        count += 1

def printBeam(end):
    print(" - - - - +", end=end)

def printBeams(cols):

    # get beam started with left '+'
    print('+', end='')

    col = 0
    while col < cols:
        if col == cols - 1:
            end = '\n'
        else:
            end = ''
        printBeam(end)
        col += 1

def printPosts(cols):
    count = 0
    while count < 4:
        printRowOfPosts(cols)
        count += 1

def printRowOfPosts(cols):
    print('/' + (' ' * 9 + '/') * cols)

def printRow(cols):
    # draw one row's worth of posts for as many columns as we have
    printPosts(cols)

    # draw another line of beams
    printBeams(cols)

drawGrid(4,0)