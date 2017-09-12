from __future__ import division
from pylab import imshow,show,hot,jet
import numpy as np
import math

N = int(raw_input("Grid Size:   "))       # gridsize
maxiter = int(raw_input("Maximum Iterations:  "))         # maxiterations

def mandelbrot(maxiter, N):
    a = np.zeros((N,N), dtype=int)
    i = 0
    k = 0
    step = 4/N
    for i in range(0,N):
        for k in range(0,N):
            iter  = 0
            z = complex(0,0) 
            c = complex(-2+i*step,2-k*step)
            for  iter in range(1,maxiter):
                if (abs(z) <= 2):
                    z = z*z + c
                    iter = iter + 1
                else:
                    break
            a[k,i] = math.log(iter,1.15)
    return a

data = mandelbrot(maxiter, N)
imshow(data)
jet()
show()


    
