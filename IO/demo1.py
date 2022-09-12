import numpy as np

# 读写文件数据的两个主要函数
# load save
# numpy.save(file, arr, allow_pickle=Ture, fix_imports = True)

x = np.arange(120000)
print(x)
np.save("aa", x)

y = np.load("aa.npy")
print(y)

# 将多个数组写入文件, 默认情况下....
# savez  loadz
a = np.array(100)
b = np.array(100)
c = np.array(100)
np.savez("abc", a, b, c)

d = np.load("abc.npz")
print(d)
print(d["arr_0"])

# savetxt
# loadtxt
m = np.arange(190)
np.savetxt("fk", m)
