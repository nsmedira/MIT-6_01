# Fermat’s Last Theorem says that there are no integers a, b, and c such that

# a**n + b**n = c**n 

# for any values of n greater than 2.

# Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.

from fermat_1 import check_fermat

def collect_check():
    user_inputs = collect_inputs(['a', 'b', 'c', 'n'])
    if user_inputs == 'q':
        print("quitting program...")
        return
    check_fermat(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3])

def collect_inputs(variables):
    user_inputs = []
    for var in variables:
        result = prompt(var)
        if result == 'q':
            return 'q'
        else:
            user_inputs.append(result)
    return user_inputs

def prompt(var):

    print("Enter a value for", var + ":")

    # get user input
    userInput = input()

    # quit program
    if userInput == 'q':
        return 'q'

    check = to_integer(userInput)

    if check == 'error':
        return prompt(var)
    else:
        return check

def to_integer(str):
    try:
        conversion = int(str)
        return conversion
    except ValueError:
        print("Your input can't be converted to an integer. Try again. Enter 'q' to quit.")
        return 'error'

# collect_check()