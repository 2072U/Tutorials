# CSCI / MATH 2072U -- Computational Science 1
# Date: 1/13/2021
# Tutorial 1, Part B
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007


import bisection
import math
def func(x,a):  # Function for bisection.
    return (x**2)-a

print("--Bisection--\n")
    x,err,res=bisection(-10,10,5,30,1e-3,1e-3,func)# Call Bisection using Recursion
print ("Solution is " +str(x) + " +/- " + str(err)+ " with residual " +str(res) ) # Add the missing variables.
