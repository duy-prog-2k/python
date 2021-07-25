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

# remove specified item 
items = ['Duy', 'Khac', 1]
items.remove(1)
print(items)

# remove specified index 
items.pop(1)
print(items)

# del keyword
newList = [1, 2, 3, 4, 5]
del newList[0]
print(newList)

# del completely list, can't reuse this list
# del newList
# another way, but clear() method return an empty list

newList.clear()
print(newList)

