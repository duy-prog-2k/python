import numpy as np 

arr = np.array([1, 2, 4, 6, 7])

# Filter sử dụng boolean index list
# boolean index list sẽ tương ứng với các phần tử có trong mảng gốc
# nếu phần tử tương ứng có giá trị là true thì mảng mới sẽ chứa phần tử đó và ngược lại. 
x = [True, False, False, True, True]

new_arr = arr[x]
print(new_arr)

# Create the filter array 
# Ví dụ: tạo một filter chỉ chứa các phần tử chia hết cho 2

filter_array = [] 

root_array = np.array([1, 2, 3, 4 ,5, 6, 7, 8])

for e in root_array: 
  if e % 2 == 0:
    filter_array.append(True)
  else: 
    filter_array.append(False)

new_arr = root_array[filter_array]
print(new_arr)

# Tạo filter trực tiếp

filter_array = root_array % 2 == 0
print(root_array[filter_array])