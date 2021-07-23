import numpy as np 

arr = np.array([1,2,3,4,5,6,7]) 
print(arr[1:5]) 

# slice elements from index 4 to the end

print(arr[4:])

# slice elements from the start to index 3 
print(arr[:4])

# slide from the index 3 from the end to index 1 from the end

print(arr[-3:-1])
