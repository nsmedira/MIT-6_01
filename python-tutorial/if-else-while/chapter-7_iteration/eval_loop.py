# Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of the last expression it evaluated.

def eval_loop():

    result = None

    while True:
        print("Enter an expression to evaluate:")
        entry = input()

        if entry == "done":
            break
        
        try:
            result = eval(entry)
            print(result)

        except:
            print('oops, couldn\'t evalute that one. try again.')

    if result == None:
        return "no expressions evaluated"
    else:
        return result

print(eval_loop())