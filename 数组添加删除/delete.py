import numpy as np

x = np.arange(12).reshape(3, 4)
print(x)

# delete(arr, obj, axis = None)


print('\n')

# 第二个参数是下标
a = np.delete(x, 4)
print(a)
print(x)
print(a.shape)

#
b = np.delete(x, 1, axis=1)
print(b)
print(b.shape)
