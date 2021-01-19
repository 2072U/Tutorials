# A mystery script. In tutorial 2 you will be challenged to find out what it does and what you can learn from it.
# By L. van Veen, Ontario Tech University, 2020.
import numpy as np
from Newton import Newton
import matplotlib.pyplot as plt

r1 = 0.2
r2 = 0.5
r3 = 0.9
def f(x):
    return (x-r1)*(x-r2)*(x-r3)

def df(x):
    return (x-r2)*(x-r3)+(x-r1)*(x-r3)+(x-r1)*(x-r2)

N = 1000
l = 0.0
r = 1.0
x0 = np.linspace(l,r,N)

kMax = 10
epsx = 1e-6
epsf = 1e-6

fig_width = 6.0
fig_height = 1.0
w = 72.0*fig_width/float(N)
fig = plt.figure(figsize=[fig_width,fig_height])
plt.xlim(l,r)
plt.ylim(0,1)
plt.xticks([])
plt.yticks([])
for k in range(N):
    x,err,res,conv = Newton(f,df,x0[k],kMax,epsx,epsf)
    if conv == 0:
        c = "k"
    else:
        if abs(x-r1) < 10*epsx:
            c = 'r'
        else:
            if abs(x-r2) < 10*epsx:
                c = 'g'
            else:
                if abs(x-r3) < 10*epsx:
                    c = 'b'
    plt.plot([x0[k],x0[k]],[0,1],color=c,linewidth=w)

plt.show()

