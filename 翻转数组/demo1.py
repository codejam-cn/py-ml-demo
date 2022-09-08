import numpy as np

a = np.arange(12).reshape(3, 4)

print(a)

# T
b = np.transpose(a)
print(b)

# 看球不懂
# rollaxis(a,axis,start)
# 向后滚动特定的轴到一个特定位置
c = np.arange(24).reshape(2, 3, 4)
print(c)

print("------")

d = np.rollaxis(c, 1)
print(d)



# swapaxes()
#
