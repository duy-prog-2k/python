# - Tuple is a collection which is ordered and unchangeable 
tuple_a = ('apple', 'banana', 'strawberry')
print(tuple_a)  

# Tuple items are ordered, unchangeable and allow duplicate values
print(len(tuple_a))

# when create tuple with one items, add a comma after this item 
thistuple = (2,)
print(type(thistuple))

thistuple = (2) 
print(type(thistuple)) # return int 

tuple_b = tuple(('apple', 'cherry', 'mango')) #double bracket
print(tuple_b)

# access a tuple
print(tuple_b[1])

# tuple can be accessed and using range of index like list collection 
#  