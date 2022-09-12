import numpy as np

# 赋值
x = np.array([1, 2, 3, 4, 5, 6])
print(x)

print(id(x))

y = x
print(y)
print(id(y))

# 视图 (浅拷贝)

