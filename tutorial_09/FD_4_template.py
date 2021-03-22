# Template for a function that 1. computes the fourth-order polynomial interplant on 5 consecutive grid points
# 2. compute its derivative and 3. returns the value of the derivative at the mid point.
import scipy
import scipy.interpolate

# Input: lists of x and y values of the interpolation nodes. Output: approximate derivative at the middle grid point.
def FD_4(xs,ys):
    n=len(xs)-1                                                  # Extract the index of the last interpolation node (grid points are labeled 0..n)
    dys = scipy.zeros(n+1)                                       # Pre-allocate array of derivatives
    for k in range(2,n-1):                                       # Loop over interior grid points (i.e. skip two points at either end)
        P = scipy.interpolate.lagrange( ... )                    # Compute local fourth-order interpolant
        dP = P.deriv()                                           # Compute its derivative
        dys[k] = dP.__call__(xs[k])                              # Evaluate the derivative at the mid point x[k]
    return dys
