# CSCI / MATH 2072U -- Computational Science 1
# Date: 02/01/2021
# Tutorial 3
# PA=LU decomposition that keeps track of the parity of the permutation (even=1, odd=-1)
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007

import scipy
import scipy.linalg
from copy import copy

# Note: indices i,j and k are used as matrix indeces (starting from 1) while s is used as python array index (starting from 0)
def LUP(A):
    n = scipy.shape(A)[0]                         # extract matrix size
    U = copy(A)                                   # copy content of A (avoid linking U and A)
    L = scipy.identity(n)                         # initialize L and P
    P = scipy.identity(n)

    for k in range(# Decide the range):
        # find pivot element

        if #condition:                            # if the pivot is not on the diagonal...
            # swap rows of U
            if #condition:                        # swap rows of L left of diagonal element
                # Your code goes here
            # swap rows of P
        for j in range(# Decide the range):       # Gauss elimination of rows below pivot
            # Your code goes here


    return L,U,P


def swap(M,i,j,k):
# Swap rows i and j from column 0 up to (but not including) k
# Indices in this function are used as python array indeces (starting from 0)

    # Your code here

    return M
