import numpy as np

a = np.arange(12)
a = a.reshape(3, 4)
print(a)

print(a.T)

print("-------------")

for x in a.T:
    print(x)
