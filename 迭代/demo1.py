import numpy as np

a = np.arange(12)
b = a.reshape(3, 4)
print(b)

for x in np.nditer(b):
    print(x, end=", ")

print("")
