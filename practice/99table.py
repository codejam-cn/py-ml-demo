# 搞一个九九乘法表看看

import numpy as np

for i in range(1, 10):
    for j in range(1, 10):
        if j >= i:
            print(i, "*", j, "=", i * j, ",", end='')
            if j == 9:
                print('')

print('\n')

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "*", i, "=", i * j, ",", end='')
        if i == j:
            print('')
