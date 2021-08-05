import numpy as np 

# 1D iterating 
arr1d = np.array([1, 2, 3])
for x in arr1d: 
  print(x)

# 2D iterating 
arr2d = np.array([[1, 2, 3], [3, 4, 5]])
for x in arr2d:
  print(x)
  for y in x: 
    print(y)

# iterating using nditer() 
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr3d):
  print(x)

# Lặp bằng liệt kê 
for idx, x in np.ndenumerate(arr1d):
  print(idx, x)

for idx, x in np.ndenumerate(arr2d):
  print(idx, x)
  