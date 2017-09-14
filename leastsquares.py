from __future__ import division
import numpy as np
from pylab import scatter,imshow,show,plot,xlabel,ylabel,xlim,ylim,suptitle

a = np.loadtxt("millikan.txt",float)                                    # imports data from the txt files
x = a[:,0]*10**-14                                                      # imports the frequency  values into an array named x, normalized to get rid of 10^-14 offset
y = a[:,1]                                                              # import voltages to y
N = len(x)                                                              # gets the length to be used for later

Ex = np.sum(x)/N                                                        # calculates values needed for getting best fit parameters 
Ey = np.sum(y)/N
Exx = np.sum(x*x)/N
Exy = np.sum(x*y)/N

m = (Exy-Ex*Ey)/(Exx-Ex*Ex)                                             # calculates best fit parameters
c = (Exx*Ey-Ex*Exy)/(Exx-Ex*Ex)

pred = [m*i+c for i in x]                                               # predicts values for each voltage based on best fit, was important in code testing
h = m*16.02                                                             # calculates h from the slope of the best fit
hquote = 6.262                                                          # quoted value of planck's constant
pd = 100*(h-hquote)/hquote                                              # calculates and displays the percent error of planck's constant
print "%(h)f 10^-34 J*s" % {"h":h}
print "This is %(pd)f percent different from" % {"pd": pd}
print "current quoted values of Planck's constant"
scatter(x,y)                                                            # displays graphs
plot(x,pred)
xlabel("Frequency (10^14 Hz)")
ylabel("Stopping Voltage (V)")
suptitle("Frequency v. Stopping Voltage from the Millikan Oil Drop experiment")
show()
