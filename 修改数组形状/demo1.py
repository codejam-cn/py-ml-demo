import numpy as np

a = np.arange(12)
print(a)

b = a.reshape(3, 4);
print(b)

for x in b.flat:
    print(x)

d = b.flatten();
print(d)

# reval
# faltten
