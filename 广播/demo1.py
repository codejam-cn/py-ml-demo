import numpy as np

a = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300], [1000, 2000, 3000]])
print(a)

b = np.array([1, 2, 3])
print(b)

c = a + b
print(c)

print(a.ndim, b.ndim, c.ndim);
print(a.shape, b.shape, c.shape);

# 让所有输入数组都向其中形状最长的数组看齐
# 输出数组的性值是输入数组各个维度上的最大值
# 如果输入shu'zu