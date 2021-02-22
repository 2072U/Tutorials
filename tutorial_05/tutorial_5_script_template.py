import numpy
import matplotlib.pyplot as plt          # For plotting

smin = 9                                 # Set minimal and maximal matrix size
smax = 15
rrs = numpy.ones(smax-smin+1)            # Pre-allocate arrays for relative residual,
res = numpy.ones(smax-smin+1)            # relative error and
mes = numpy.ones(smax-smin+1)            # maximal error

for n in range(smin,smax+1):             # Loop over matrix sizes
    xe = numpy.zeros((n,1))              # Exact solution
    xe[0] = 1.0         
    A = numpy.zeros((n,n))               # Allocate and fill A
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i-1,j-1] = # insert matrix elements
    r =                  # set right-hand side
    x =                  # solve by LU decomposition (use our won LUP code or np.linalg.solve)

    rrs[n-smin] = # compute the relative residual
    res[n-smin] = # compute the relative error
    mes[n-smin] = # condition number times the relative residual (equals the maximal relative error)


plt.semilogy(range(smin,smax+1),res,'-b',range(smin,smax+1),mes,'-r')
plt.xlim([smin,smax])
plt.xlabel('matrix size')
plt.ylabel('(maximal) relative error')
plt.title('Maximal (red) and actual (blue) relative error')
plt.show()
