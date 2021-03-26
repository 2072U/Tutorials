# Script to test the higher-order finite differnce function
import scipy
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preview'] = True
import matplotlib.pyplot as plt          # For plotting

from FD_4_template import FD_4

# Test function and its derivative
def f(x):
    return x * scipy.sin(5.0 * x)

def df(x):
    return scipy.sin(5.0 * x) + 5.0 * x * scipy.cos(5.0 * x)

r = scipy.pi
l = 0.0

err_centered_diff = scipy.zeros((0,2))
err_interpolant = scipy.zeros((0,2))                      # Start with empty array for errors

for i in range(3,11):
    N = 2**i                                              # Loop up to N=2^10
    h = (r - l)/float(N)                                  # grid spacing
    x_grid = scipy.linspace(l, r, N+1)                    # Set up equidistant grid
    y_exact = f(x_grid)                                   # Evaluate test function on grid (vectorized!)
    dy_exact = df(x_grid)                                 # Compute derivatives from analytic expression

# centered finite differences
    dy_centered_diff = scipy.zeros(y_exact.size)
    for j in range(1,N):
        dy_centered_diff[j] = (y_exact[j+1] - y_exact[j-1]) / (2.0*h)

    err_centered_diff = scipy.append(err_centered_diff, [[h, scipy.linalg.norm(dy_centered_diff[1:N] - dy_exact[1:N], scipy.inf)]], 0)

# higher order finite differences
    dy_interpolant = FD_4(x_grid,y_exact)                 # Call interpolation function

# Compute error and grid spacing
    err_interpolant = scipy.append(err_interpolant, [[h, scipy.linalg.norm(dy_interpolant[2:N-1] - dy_exact[2:N-1], scipy.inf)]], 0 )

# Print and plot errors, compare to h^{-4} decay.
# print err_centered_diff
# print err_interpolant
plt.loglog(err_centered_diff[:,0],err_centered_diff[:,1],'-*', label='Centered Finite Difference')
plt.loglog(err_interpolant[:,0],1000.0*err_interpolant[:,0]**2, label=r'$O(h^2)$')
plt.loglog(err_interpolant[:,0],err_interpolant[:,1],'-o', label='Interpolant')
plt.loglog(err_interpolant[:,0],1000.0*err_interpolant[:,0]**4, label=r'$O(h^4)$')
plt.xlabel('Grid size')
plt.ylabel('Error')
plt.legend(loc ="lower right")
# plt.title('Green is O(h^2), black is O(h^4)')
plt.show()
