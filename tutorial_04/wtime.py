# Template of a script for comparing the wall time it takes to compute the determinant of a matrix recursively and using LUP decomposition. Tutorial 4, MATH/CSCI2072U, 2021.
import numpy as np
from deter_LUP import deter_LUP
from deter_recur import deter_recur
from time import time
import matplotlib.pyplot as plt

n_start = 2
n_end = 9
wtime_recur = np.array((n_end-n_start+1,2))
wtime_LUP = np.array((n_end-n_start+1,2))

for n in range(n_start,n_end+1):
    # Create random nXn array:
    A = 
    # Compute the determinant recursively:
    start_time = # Get current time.
    det = deter_recur(A)
    end_time = # Get current time.
    wtime_recur[ ... ]  = # Store wall time.
    # Compute the determinant using LUP decomposition:
    start_time = # Get current time.
    det = deter_LUP(A)
    end_time = # Get current time.
    wtime_LUP[ ... ]  = # Store wall time.

# Plot the results (experiment with log/linear scales!).
plt.plot(wtime_recur[ ...] ...)
plt.plot(wtime_LUP[ ...] ...)
plt.show()
