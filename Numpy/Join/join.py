import numpy as np
# join two array 
arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 4, 6])
arr = np.concatenate((arr1, arr2)) 
print(arr)
# join two array 2d
arr3 = np.array([[1, 2, 3], [2, 3, 4]])
arr4 = np.array([[2, 5, 6], [6, 3, 8]])
arr = np.concatenate((arr3, arr4), axis = 1)
print(arr)