import numpy as np

x = np.array([1,2,3,3,3,4,5,6,6,7,8,6,5,4,5,6,78,8,7,6,55,66,6,7,7,71])
print(x)

# unique(arr, returnIndex, returnInverse, returnCounts)


print('\n')

a = np.unique(x)
print(a)


print('\n')
b = np.unique(x,return_index=True)
print(b)
