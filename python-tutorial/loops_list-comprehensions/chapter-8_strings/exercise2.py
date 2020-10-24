prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'Q':
        letter = 'Qu'
    print (letter + suffix)