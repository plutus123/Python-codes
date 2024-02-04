import numpy as np
import matplotlib.pyplot as plt
import random
mu=5
sigma=2
arr=mu+sigma*np.random.randn(1000)
# print (arr)
# histogram only takes one argument
plt.hist(arr,50)
plt.show()
arr=np.round(arr)
z=np.unique(arr,return_counts=True)
print(z)
