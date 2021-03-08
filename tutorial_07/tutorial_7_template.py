# Author: L. van Veen, Ontario Tech U, 2021.
# Template for tutorial 7 on the error of polynomial interpolation for the Runge function.
import numpy as np
import matplotlib.pyplot as plt

# Test function:
def f(x):                   
    return 1.0/(1.0+x**2)

# Domain:
l = -10.0
r = 10.0
# Grid for plotting:
n_plot = 
xs = np.linspace(l,r,n_plot) 

# Remember errors for an increasing number of nodes for plotting:
err = []

# Loop over increasing number of grid points:
for n in range(2,6):
    N = 2**n
    # x-values for interpolation:
    x = np.linspace(l,r,N)
    # Corresponding y-values:
    y = f(x) # Note that the evaluation is "vectorized", a loop over elements of x is implied.
    # Compute the interpolant and evaluate it on the fine grid for comparison:
    ys =                  # Call our own function(s) or one of NumPy's built-in interpolation functions.
    
    plt.plot(xs,f(xs),'-k',xs,ys,'-r')
    plt.ylim([f(l)-1.0,f(r)+1.0])
    plt.xlabel('x')
    plt.ylabel('function and interpolant')
    plt.title('%d equidistant nodes' % (N))
    plt.show()
    e = abs(f(xs)-ys)
    err.append([N,max(e)])
    plt.plot(xs,e,'-r')
    plt.xlabel('x')
    plt.ylabel('interpolation error')
    plt.title('%d equidistant nodes' % (N))
    plt.show()

# Plot the error of interpolation versus the number of nodes:
err = np.asarray(err)
plt.loglog(err[:,0],err[:,1],'-*')
plt.show()
