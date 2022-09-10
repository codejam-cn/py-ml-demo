import numpy as np

x = np.arange(12);
print(x)

a = np.split(x,3)
print(a)

b = np.split(x,[2,5])
print(b)