import numpy as np
from LUP import LUP

def deter_LUP(A):
    L,U,P,sig = LUP(A)
    det_LUP = ... # Useful functions: np.diag, np.prod.
    return det_LUP
