import numpy as np

# 视图, 视图就是浅拷贝
x = np.arange(12)
print(x)
print(id(x))

y = x[3:]
print(y)


# 副本, 副本就是深拷贝
z = x.copy();
print(z)
print(id(z))