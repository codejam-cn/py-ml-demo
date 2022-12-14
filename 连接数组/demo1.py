import numpy as np

x = np.arange(1, 5).reshape(2, 2)
print(x)

y = np.arange(5, 9).reshape(2, 2)
print(y)

z = np.concatenate((x, y))
print(z)

# stack
print("\n")

a = np.arange(1, 5).reshape(2, 2)
print(a)
print(a.shape)
print(a.ndim)

b = np.arange(5, 9).reshape(2, 2)
print(b)
print(b.shape)
print(b.ndim)

c = np.stack((a, b), 0)
print(c)
print(c.shape)
print(c.ndim)

d = np.stack((a, b), 1)
print(d)
print(d.shape)
print(d.ndim)

print("------------------------ \n")
# hstack
# vstack