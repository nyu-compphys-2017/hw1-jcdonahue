from __future__ import division
import numpy as np
from pylab import scatter,imshow,show,plot

a = np.loadtxt("millikan.txt",float)
x = a[:,0]*10**-14
y = a[:,1]
N = len(x)

Ex = np.sum(x)/N
Ey = np.sum(y)/N
Exx = np.sum(x*x)/N
Exy = np.sum(x*y)/N

m = (Exy-Ex*Ey)/(Exx-Ex*Ex)
c = (Exx*Ey-Ex*Exy)/(Exx-Ex*Ex)

pred = [m*i+c for i in x]
h = m*16.02
hquote = 6.262
pd = 100*(h-hquote)/hquote
print "%(h)f 10^-34 J*s" % {"h":h}
print "This is %(pd)f percent different from" % {"pd": pd}
print "current quoted values of Planck's constant"
scatter(x,y)
plot(x,pred)
show()
