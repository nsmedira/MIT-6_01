# Fermat’s Last Theorem says that there are no integers a, b, and c such that

# a**n + b**n = c**n 

# for any values of n greater than 2.

# Write a function named check_fermat that takes four parameters—a, b, c and n—and that checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that

# a**n + b**n = c**n 

# the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

# this is true of n=2, but doesn't disprove fermat's last theorem
# check_fermat(3, 4, 5, 2)