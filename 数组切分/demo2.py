import numpy as np

x = np.arange(12).reshape(3, 4)
print(x)

a = np.split(x, 3)

print(a)

#
b = np.split(x, 2, axis=1)

print(b)

# hsplit
c = np.hsplit(x, 3)
print(c)


#vsplit