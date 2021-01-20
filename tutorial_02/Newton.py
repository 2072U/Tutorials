#Author: Lennaert van Veen
#Date: 1/17/2017
# Python function for Newton iteration
import math

def Newton(f,df,x0, kMax, epsX, epsF):
# Input: initial point, max nr. of iterations, tolerance for error and residual
    x=x0
    conv=0                         # flag for convergence
    for k in range(1,kMax):
        fx=f(x)                 # current function value
        dx=-fx/df(x)            # update step
        err = abs(dx)              # current error estimate
        res = abs(fx)              # current residual
#        print("Iteration "+str(k)+" err="+str(err)+" res="+str(res))        
        if err < epsX and res < epsF:       # If converged ...
#            print("Converged!")
            conv=1
            break
        x=x+dx
    
#    if conv==0:
#        print("No convergence!")
    return x,err,res,conv


