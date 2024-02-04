import matplotlib.pyplot as plt
import numpy as np
b=[1,2,1,3,5,4,5,5,4,3,3,10,7,6,7,8,8,20,22,11,14]
xt=np.arange(23)
plt.xticks(xt)
bins=[1]
plt.hist(b,edgecolor="black",color='cyan',bins=21)
plt.axis([0,25,0,5])
plt.show()