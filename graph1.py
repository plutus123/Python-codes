import numpy as np
import matplotlib.pyplot as plt
# x=np.array([1,2,3,4,5,6,7,8,9,10])
# y=np.array([1,2,5,10,17,26,37,50,82,101])
# plt.plot(x,y)
# plt.grid()
# plt.show()
x=np.arange(0,20,2)
y=2**x
plt.plot(x,y,"b--",label="2**x")
plt.legend()
plt.show()
