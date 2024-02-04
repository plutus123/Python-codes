import numpy as np
import matplotlib.pyplot as plt
mean=np.array([0,0])
cov=np.array([[1,0],[0,1]])
dist=np.random.multivariate_normal(mean,cov,500)
# print(dist)
plt.scatter(dist[:,0],dist[:,1])
plt.show()