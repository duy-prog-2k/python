import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()

x[0] = 42  
# Thay doi cua mang copy khong lam anh huong den original array 
print("Mang ban dau khong bi anh huong khi phan tu cua mang copy thay doi: ",arr)
print("Mang copy: ", x)

# thay doi mang goc lam thay doi mang view 
y = arr.view()
print("Mang view khi mang ban dau chua bi sua doi",y)
print("Mang ban dau ", arr) 
arr[0] = 44 
print("Mang ban dau sau khi sua phan tu thu 0", arr) 
print("Mang view cung bi thay doi do bi anh huong boi original array", y) 
