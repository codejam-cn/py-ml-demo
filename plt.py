import numpy as np
from matplotlib import pyplot as plt

min_limit = -np.pi
max_limit = np.pi

x = np.arange(min_limit, max_limit, 0.1)

y1 = np.sin(0.5 * x)
y2 = np.cos(x)


plt.subplot(1, 1, 1)
plt.plot(x, y1)
plt.title("sin")

# plt.subplot(2,2,2)
plt.plot(x, y2)
plt.title("cos")

plt.show()
