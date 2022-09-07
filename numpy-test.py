import numpy as np

# object 要转换为的数据类型对象
# 如果为true,填充字段使其类似C结构体
# 复制dtype对象,如果false,则是对内置数据类型对象的引用
# np.dtype(object,align,copy)

dt = np.dtype(np.int32)
# print(dt)
# print(type)

student = np.dtype([("aa", "S10"), ("11", "i4")])
print(student)
