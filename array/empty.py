import decimal

import numpy as np

# np.empty(shape, dtype, order) 也可以用于创建数组
# shape 数组形状
# 数据类型, 可选
# 有 C 和 F两个, 分别代表行优先和列优先, 在计算机内存中的存储顺序

arr = np.empty([30, 20], dtype=int)
print(arr)

# zeros(shape,dtype,order)
arr2 = np.zeros([10, 4], dtype=decimal.Decimal)
print(arr2)

arr3 = np.zeros(5, dtype=decimal.Decimal)
print(arr3)

arr4 = np.zeros(5, dtype=[('x', 'i4')])
print(arr4)

## np.ones()

arr5 = np.ones([3, 3], dtype=int)
print(arr5)

## np.full(shape,fillvalue,dtype,order)

