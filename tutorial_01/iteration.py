# CSCI / MATH 2072U -- Computational Science 1
# Date: 1/13/2021
# Tutorial 1, Part A
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007


# Implementation of the iterative computation of a square root.
# In: x, initial point; a, parameter; k_max, max nr of iterations
# Out: x, approximation of sqrt(a)
def iteration(x, a, k_max):
    y=x
    for k in range(k_max):
            y = map(y,a)
            print("Current approximation = " + str(y))
                                 # Apply map to evaluate the current approximation
    

    # Iterate to find successive approximations

    return y                            # Decide the function to return

# Map that produces iterates converging to sqrt(a)
def map(x, a):
    return 0.5*(x+(a/x))

# Execution part of code
print("Fixed point iteration")
 g=iteration(3,5,15)       #  Call the function with suitable values
print ("Solution is " + str(g))               # Add the value to be printed
