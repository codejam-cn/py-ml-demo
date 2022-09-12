import numpy as np

# quicksort

# sort(a,axis,kind,order)
x = np.random.randint(1, 11, 12).reshape(3, 4)
print(x)

print('\n')

a = np.sort(x)
print(a)

print('\n')
b = np.sort(x, axis=0)
print(b)

print('\n')
dt = np.dtype([("name", "S10"), ("age", int)])
y = np.array([("ldh", 34), ("zxy", 23), ("liubd", 112)], dtype=dt)
print(y)

print('\n')
c = np.sort(y, order="age")
print(c)

# argsort()  对输入数组沿给定轴间接排序, 并使用值定排序类型返回数据的索引数组
print('\n')
x = np.array([3, 1, 2])
m = np.argsort(x)
print(m)
n = x[m];
print(n)

# lexsort() 使用键序列间接排序,
# 如考试, 按总成绩排序.  总成绩相同时, 物理成绩高的优先录取; 然后...英语.....
print('\n')
nm = ("raju", "anli", "ravi", "amar")
dv = ("f.y", "s.y", "s.y", "f.y")
res = np.lexsort((dv, nm))
print(res)

# msort
# sort_complex(a) 将复数,按照先实部后虚部的方式排序

# 指定一个数, 对数组进行分区
# partition(a, kth,[, axis, kind, order])


#
# argpartition(a, kth, [,axis, kind, order])


# meregesort

# heapsort
