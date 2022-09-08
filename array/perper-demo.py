import numpy as np

arr = np.arange(24)
print(arr)
print(arr.size)
print(arr.shape)
print(arr.ndim)

arr2 = arr.reshape(2, 3, 4)
print(arr2)
print(arr2.itemsize)