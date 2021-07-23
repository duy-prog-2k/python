import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Tạo ra mảng 2 chiều từ mảng 1 chiều
# Tạo ra mảng 4 chiều mỗi chiều có 3 phần tử từ mảng cũ 
newArr = arr.reshape(4, 3) 
print(newArr)

#Tạo ra mảng 3 chiều từ mảng 1 chiều

newArr = arr.reshape(2, 3, 2) 
print(newArr)