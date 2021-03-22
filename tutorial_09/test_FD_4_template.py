# Script to test the higher-order finite differnce function
import scipy
import matplotlib.pyplot as plt          # For plotting

from FD_4 import FD_4

# Test function and its derivative
def f(x):
    return x * scipy.sin(5.0*x)

def df(x):
    return scipy.sin(5.0*x)+ 5.0 * x * scipy.cos(5.0*x)

errsc = scipy.zeros((0,2))
errs = scipy.zeros((0,2))                                 # Start with empy array for errors
for i in range(3,12):
    N =                                                   # Loop up to N=2^10
    h =                                                   # grid spacing
    xs = scipy.linspace( ... )                            # Set up equidistant grid
    ys = f(xs)                                            # Evaluate test function on grid (vectorized!)
    dye = df(xs)                                          # Compute derivatives from analytic expression
# centered finite differences
    dysc = scipy.zeros(ys.size)
    for j in range(1,N):
        dysc[j] = ...
        
    errsc = scipy.append(errsc, ... )
# higher order finite differences
    dys = FD_4(xs,ys)                                     # Call interpolation function
# Compute error and grid spacing
    errs = scipy.append(errs, ... )

# Print and plot errors, compare to h^{-4} decay.
print errsc
print errs
plt. ... (errsc[:,0],errsc[:,1],'-r*',errs[:,0],1000.0*errs[:,0]**2,'-g')
plt. ... (errs[:,0],errs[:,1],'-r*',errs[:,0],1000.0*errs[:,0]**4,'-k')
plt.xlabel('h')
plt.ylabel('Finite difference error')
plt.title('Green is O(h^2), black is O(h^4)')
plt.show()
