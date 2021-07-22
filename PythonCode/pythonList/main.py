# List item duoc sap xep, co the thay doi, va cho phep cac gia tri trung nhau 
# List co the chua cac kieu du lieu khac nhau 
listA = ['apple', 'mango', 'banana'];
listA[1] = 'Dau tay'
print(listA)

# list len 
print(len(listA))

# use list constructor to create a list 
listB = list(('Pham', 'Khac', 'Duy'))
print(listB)

# add element to list 
listB.append('Keke')
print(listB)

# insert element to a specified index 
listB.insert(1, 'Van')
print(listB)

# extend a list 
listB.extend(listA)
print(listB)