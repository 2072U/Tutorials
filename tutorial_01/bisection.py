# Author: Lennaert van Veen, Ontario Tech U
# Date: 1/13/2020
# Python function for bisection, programmed recursively.
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007

# Approximates the solution to func(x)=0 by bisection.
def bisection(l, r, a, kMax, epsX, epsF, func):
# Input: initial left and right boundary, max nr. of iterations, tolerance for error and residual, function handle.
    m = (l+r)/2                # Compute midpoint.
    err = abs(r-l)/2           # Compute current error.
    fm = func(m,a)               # Compute function value at mid point.
    res = abs(fm)              # Compute current residual.
    x=m                        # Set surrent approximation.
    print("l="+str(l)+" r="+str(r))
    if (kMax > 0):             # If number of iterations is not exceeded...
        if err > epsX or res > epsF:       # If not converged yet...
            fl = func(l)       # Compute function value at left boundary.
            if (fm*fl > 0):
                l = m          # Discard left half.
            else:
                r = m          # Discard right half.
            x,err,res = bisection(l, r, kMax-1, epsX, epsF, func) # Recursive call.
    else:
        print("Warning: maximal number of iterations exceeded...")

    return x,err,res
