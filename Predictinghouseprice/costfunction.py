import numpy as np

#cost function

def costfunction1(x,y,Theta):


    m=x[:,0].size

    h = np.matmul(x,Theta)
    diff = (h-y)
    sdiff = np.multiply(diff,diff)
    s = np.sum(sdiff)
    j=(0.5*(1/m)*s)
    return j



