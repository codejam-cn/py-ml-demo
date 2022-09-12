import numpy as np

x = np.random.randint(1, 15, size=12)
print(x)
y = x.reshape(3, 4)
print(y)

print()
print(y.shape)
print(y.shape[0])
print(y.shape[1])

a = range(y.shape[1])
print(a)

print()
for i in range(y.shape[1]):
    for j in range(y.shape[0]):
        print(y[j, i])
