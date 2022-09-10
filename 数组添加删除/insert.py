import numpy as np

x = np.arange(6).reshape(2, 3)
print(x)

# insert(arr, obj, values, axis = None)
# arr 输入数组
# obj 在其之前插入值的索引
# values， 要向arr添加的值，需要形状相同 （除了要添加的轴）
# axis无定义时，横向加成，返回总是为一维数组！
# 当axis有定义的时候， 分别为0和1的时候。
#

print('\n')

a = np.insert(x, 3, [11, 22])
print(a)
print(a.shape)
