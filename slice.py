import numpy as np

arr = np.arange(0, 100, 1)
print(arr)

c = slice(10, 20, 2)
print(arr[c])
print(arr[20:30:1])

arr.shape = (5, 20)
print(arr)


