import matplotlib.pyplot as plt
import numpy as np
t=np.zeros((5,5,3),dtype=int)
t[:,:,2]=255
plt.imshow(t)
plt.show()
