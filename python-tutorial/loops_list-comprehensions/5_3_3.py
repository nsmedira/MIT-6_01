def cat6(t):

    # In Python you can use + to concatenate two lists. 
    # Write a procedure, called cat6(l) that takes a list 
    # as an argument and returns a list with the integer 6 
    # concatenated to the end; 
    # the output will be a list with one more element that the input. 

    return t + [6]

if __name__ == "__main__":
    print(cat6([1, 2, 3, 4, 5]))