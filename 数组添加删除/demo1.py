import numpy as np

x = np.arange(6).reshape(2, 3)
print(x)

print('\n')

# resize
y = np.resize(x, (3, 2))
print(y)

#
print('\n')
z = np.resize(x, (3, 4))
print(z)
