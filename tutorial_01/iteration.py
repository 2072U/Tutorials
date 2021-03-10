# CSCI / MATH 2072U -- Computational Science 1
# Date: 1/13/2021
# Tutorial 1, Part A
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007


# Implementation of the iterative computation of a square root.
# In: x, initial point; a, parameter; k_max, max nr of iterations
# Out: x, approximation of sqrt(a)
def iteration(x, a, k_max,eps):
    y=x
    for k in range(k_max):
        z=y
        y=map(y,a)
        if (y-z)>0:
            if (y-z)<eps:
                print("Entered within error zone")
                break
        else:
            if (y-z)>eps:
                print("Entered within error zone")
                break
        print ("Current approximation = " + str(y))
        

    # Iterate to find successive approximations

    return  y                            # Decide the function to return

# Map that produces iterates converging to sqrt(a)
def map(x, a):
    return 0.5*(x+(a/x))

# Execution part of code
print("Fixed point iteration")
      q=iteration(3,9,10,0.02)  #  Call the function with suitable values
print ("Solution is " +str(q) )               # Add the value to be printed
