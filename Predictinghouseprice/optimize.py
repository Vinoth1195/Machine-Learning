import numpy as np
from costfunction import costfunction1
def optimize(x,y,Theta,alpha):

        for i in range(1499):

            m = x[:, 0].size
            h = np.matmul(x, Theta)
            diff = np.matmul(np.transpose(x),(h-y))
            Theta = Theta-(alpha*(1/m)*diff)

            #print(j)

        j = costfunction1(x, y, Theta)
        #print("Cost function after training",j)
        return Theta











