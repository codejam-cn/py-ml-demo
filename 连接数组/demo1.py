import numpy as np

x = np.arange(1, 5).reshape(2, 2)
print(x)

y = np.arange(5, 9).reshape(2, 2)
print(y)

z = np.concatenate((x, y))
print(z)
