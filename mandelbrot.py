from __future__ import division
from pylab import imshow,show,hot,jet,xlabel,ylabel,suptitle
import numpy as np
import math

N = int(raw_input("Grid Size:   "))       # user sets gridsize
maxiter = int(raw_input("Maximum Iterations:  "))         # user sets maxiterations

def mandelbrot(maxiter, N):                         # function to create mandelbrot set
    a = np.zeros((N,N), dtype=int)                  # initialize NxN array with all zeros
    i = 0                                           # initialize i and k at zero, they will be indexes that run over the array
    k = 0
    step = 4/N                                      # calculates the step size to break up the 4x4 sqaure of values we want to calculate the set for
    for i in range(0,N):                            # these for loops run the mandelbrot test over each entry in the array
        for k in range(0,N):
            iter  = 0                               # initialize iterations and z at zero
            z = complex(0,0) 
            c = complex(-2+i*step,2-k*step)         # set c, the variable in the iterated map. This will choose values in an NxN square superimposed on the 4x4 sqaure
            for  iter in range(1,maxiter):          # have the for loop run up until the max iter set by the user
                if (abs(z) <= 2):                   
                    z = z*z + c                     # sqaures z and adds c until the absoulte value of z exceedes 2, then breaks the for loop.
                    iter = iter + 1                 # this preserves the number of iterations it took to exceed 2
                else:
                    break
            a[k,i] = math.log(iter,1.15)            # this then sets the value of the array entry to the log of the number of iterations. 1.15 was chosen to increase the color variations in interesting regions
    return a                                        # outputs the populated array

data = mandelbrot(maxiter, N)                      
imshow(data)
jet()                                               # runs mandelbrot with the user defined values and displays it in Jet coloring

imshow(data).axes.get_xaxis().set_ticks([])
imshow(data).axes.get_yaxis().set_ticks([])
suptitle("Mandelbrot Set")
xlabel("Real")
ylabel("Imaginary")
show()


    
