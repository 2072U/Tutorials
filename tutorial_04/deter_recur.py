import numpy as np

def det_recur(A):
    n = # Extract the number of rows/columns.
    if n == 2:
        det_recur = ... # Define the determinant for n=2.
    else:
        det_recur = 0.0
        for j in range(0,n):  # Loop over rows.
            B = # Construct sub matrix (useful function: np.delete).
            deter_recur += ... # Insert recursive call here according to the formula at point 2. on the tutorial PDF.
    return det_recur
