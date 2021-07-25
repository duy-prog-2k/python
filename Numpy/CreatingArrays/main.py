import numpy as np 

# create an array 

arr = np.array([1, 2, 3, 4, 5]) 
print(arr)

# 0-D array 
arr  = np.array(42)
print('Scalars: ',arr)

# 1-D array 
arr = np.array([1, 2, 3, 4, 5]) 
print('Mảng 1 chiều: ',arr)

# 2-D array  
arr = np.array([[1,2,4,6], [2,4,6,7]])
print('Mảng 2 chiều: ',arr)

print('Chiều của mảng là: ',arr.ndim)