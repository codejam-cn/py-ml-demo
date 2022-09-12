import numpy as np

x = np.arange(1, 10)
for i in x:
    print(i)

y = np.random.randint(1, 100, size=12)
z = np.array(y)
z.shape = (3, 4)
print(z)

print("----------------------------")

for row in z:
    print(row)

print("----------------------------")
for row in z:
    for cell in row:
        print(cell)

print("----------------------------")
m = z.transpose()
print(m)


