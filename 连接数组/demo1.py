import numpy as np

x = np.arange(1, 5).reshape(2, 2)
print(x)

y = np.arange(5, 9).reshape(2, 2)
print(y)

z = np.concatenate((x, y))
print(z)

# stack

a = np.arange(1, 5).reshape(2, 2)
print(a)
print(a.shape)
print(a.ndim)

b = np.arange(5, 9).reshape(2, 2)
print(b)
print(b.shape)
print(b.ndim)

c = np.stack((a, b))
print(c)
print(c.shape)
print(c.ndim)
