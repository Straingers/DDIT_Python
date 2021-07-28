import numpy as np

a = np.zeros((4, 4))
b = np.ones((5, 5)) * 4

print(a.shape)
print(b.shape)

c = a.reshape((16))
print(c)
