# Template for Tutorial 6 on interpolation with the Vandermonde matrix. By L. van Veen, UOIT, 2021.
import numpy as np
import matplotlib.pyplot as plt          # For plotting

def intpl(x,y):                          # Compute the Lagrange interpolating polynomial using the Vandermonde matrix
    n = np.shape(x)[0]-1                 # Order of the interpolant
    V = np.zeros((n+1,n+1))              # Allocate Vandermonde matrix
    for i in range(0,n+1):               # Compute matrix elements
        <insert code>
    print("Cond. nr. is "+str(np.linalg.cond(V))+" for n="+str(n))
    a =                                  # Solve for coefficients (use our LUP module or np.linalg.solve)
    return a

def f(x):                                # Test function
    return np.exp(x)

def P(x,a):                              # Evaluate interpolant using Horner's algorithm
    n = np.shape(a)[0]-1
    Q = a[n-1] + a[n] * x
    for k in range(n-2,-1,-1):
        Q = a[k] + Q * x
    return Q

for n in range(4,16):                    # Test for increasing number of interpolation nodes
    x = np.zeros(n+1);                   # Allocate arrays for interpolation points and values
    y = np.zeros(n+1);
    for k in range(0,n+1):               # Compute interpolation data
        x[k] = ...
        y[k] = ...
    a = intpl(x,y)                       # Compute interpolant
    
    nplot = 1000                         # Plot function and interpolant on np points between x=0 and x=n
    xs = np.zeros(nplot)                 # Allocate arrays for points to plot.
    yf = np.zeros(nplot)                 # For values of the test function f
    yp = np.zeros(nplot)                 # For values of the interpolant
    for k in range(0,nplot):
        xs[k] = ...
        yf[k] = ...
        yp[k] = ...
    plt.plot(xs,yf,'-k',xs,yp,'-r')
    plt.show()

# Once this is working, try to evaluate the error of linear solving and the interpolation error.
# For instance, you can use the inequality "rel err =< cond nr * rel res" and compute the difference between f(x) and the interpolant on a grid.
