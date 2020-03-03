import numpy as np
import matplotlib.pyplot as plt
from costfunction import costfunction1
from optimize import optimize

a = np.loadtxt(fname='ex1data1.txt',delimiter=',')

y = a[:,1]
m=a.shape
#print(m[0])
temp1=a[:,0]
temp2=np.ones(m[0])
x = np.column_stack([temp2,temp1])
Theta = np.array([0,0])

plt.plot(a[:,0],a[:,1],'x',color='red')
plt.xlabel("Population of city in 10,000s")
plt.ylabel("Profit in 10,000$")
plt.axis([4,24,-5,25])

plt.show()



J = costfunction1(x,y,Theta)
print("Costfunction before training",J)
alpha = 0.01


Theta = optimize(x,y,Theta,alpha)
print("Theta values",Theta)



plt.plot(a[:,0],a[:,1],'x',color='red')
plt.xlabel("Population of city in 10,000s")
plt.ylabel("Profit in 10,000$")
plt.plot(x[:,1],np.matmul(x,Theta))
plt.show()



print("Enter population in 10,000s")

pop = float(input())
pop=np.array(pop)
pop=np.column_stack([1,pop])
predict=np.matmul(pop,Theta)
print("Predicted profit is",predict*10000)