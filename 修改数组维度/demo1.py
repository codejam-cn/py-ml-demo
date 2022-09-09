import numpy as np

# broadcast()
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

print(x)
print(y)

z = np.broadcast(x,y)
print(z)