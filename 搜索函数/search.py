import numpy as np

x = np.array([[35, 54, 534], [55, 56, 78]])
print(x)

print(x.flatten())
print(x.flatten(order="F"))

# np.max()

# np.argmax(x)

# 返回数组中的非零元素的索引
# nonzero

print(x.nonzero())

# where
x = np.arange(-10, 30, 3)
print(x)
y = np.where(x % 2 == 0)
print(y)

#
# np.extract()

con = np.mod(x, 2) == 0
print(con)
