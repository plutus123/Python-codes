import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,10,0.1)
y=np.log(x)
plt.scatter(x,y)
# x=np.array([1,2,3])
# y=np.array([1,2,3])
plt.plot(x,y,"r--")
plt.show()