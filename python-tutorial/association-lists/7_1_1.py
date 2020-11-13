def emptyAlist():
    return []

def addEntry(al, k, v):
    return al + [[k, v]]

if __name__ == "__main__":
    print(addEntry(emptyAlist(), 'key', 'value'))