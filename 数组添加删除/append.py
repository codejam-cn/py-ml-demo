import numpy as np

x = np.arange(6).reshape(2, 3)
print(x)

# append(arr, values, axis = None)
# arr 输入数组
# values， 要向arr添加的值，需要形状相同 （除了要添加的轴）
# axis无定义时，横向加成，返回总是为一维数组！
# 当axis有定义的时候， 分别为0和1的时候。
#

print('\n')

a = np.append(x, [7, 8, 9])
print(a)
print(a.shape)

print('\n')
b = np.append(x, [[7, 8, 9]], axis=0)
print(b)
print(b.shape)

print('\n')
c = np.append(x, [[7, 8], [8, 9]], axis=1)
print(c)
print(c.shape)
