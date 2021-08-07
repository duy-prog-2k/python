import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]);
x = np.where(arr == 4); # return index of element
print(x)

# find the index where number is even 
x = np.where(arr % 2 == 0);
print(x) # return an array include index of element which is even 

# Cú pháp: np.searchsorted(array, num) 
# Thực hiện tìm vị trí mà chúng ta có thể chèn num vào mà không làm thay đổi sắp xếp của mảng 

arr = np.array([6, 7, 9])
x = np.searchsorted(arr, 8); # return 2, chèn 8 vào arr[2] sẽ đúng theo sắp xếp
print(x)

	
