def lookup(al, k):

    for i in al: 
        if i[0] == k:
            return i
    
    return None

if __name__ == "__main__":
    print(lookup([['key', 'value'], ['marco', 'polo']], 'missing'))