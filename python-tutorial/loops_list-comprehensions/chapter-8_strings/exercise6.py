from exercise4 import find

def count(string, letter):

    count = 0
    start = 0
    while True:
        index = find(string, letter, start)

        if index == -1:
            break

        count += 1
        start = index + 1

    print (count)

count('mississippi', 'm')