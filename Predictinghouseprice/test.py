import numpy as np

import matplotlib.pyplot as plt




pop = input()
z=np.array(pop)
z=np.column_stack([1,pop])
print(z)
print(z.shape)