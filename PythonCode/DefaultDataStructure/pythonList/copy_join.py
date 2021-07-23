# Khong the copy 1 list bang cach list1 = list2 vi list1 chi la reference cua list2, nhung thay doi tren list 2 cung duoc 
# ap dung tren list1
thislist= [1, 2, 3, 4, 5]
a = thislist.copy(); 

# another way 
b = list(thislist)

# join list using + operator 
list1 = list(thislist)
list2 = ['a', 'b', 'c']
list3 = list1 + list2 
print(list3)

# using extend() to add a list to another list