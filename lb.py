import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])  # 2* 3 数组

b = np.array([[1, 2, 1],
              [2, 1, 2]])  # 2* 3 数组

# 对应位置元素相加
x1 = a + b

# 数组乘法：对应位置元素相乘
x2 = a * b


# 矩阵乘法：执行矩阵乘法规则   * 是魔法化方法，判断对象是数组就执行数组乘法，判断对象是矩阵就执行矩阵乘法
x3 = np.mat(a) * np.mat(b.T)  # a 是2*3 矩阵， b。T代表b的转置 是3*2矩阵  二者相乘得到2*2矩阵

x4 = np.mat(a.T) * np.mat(b)  # 二者相乘得到3*3矩阵

# 矩阵求逆
inverse = np.linalg.inv(x4)

# 求特征值，特征向量
value, vector = np.linalg.eig(x4)

print(x1)
print(x2)
print(x3)
print(x4)
print(inverse)
print(vector)
print(value)
