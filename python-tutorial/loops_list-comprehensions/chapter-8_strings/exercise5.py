def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    print (count)

count('mississippi', 'i')