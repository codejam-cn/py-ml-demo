import numpy as np

x = np.random.randint(1, 11, 9).reshape((3, 3))
print(x)

# max min

# 计算数组中元素最大值与最小值的差
# ptp
print(np.max(x))
print(np.min(x))
print(np.ptp(x))

# 看球不懂
# percentile(a , q, axis).

# 中位数
# median

# 算数平均值
# mean

# 。。。。。 重要， 加权平均值
# average
# 也可用于多维数组

# 标准差
# sqrt

# 方差
# var
