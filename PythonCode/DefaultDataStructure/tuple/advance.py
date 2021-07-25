# tuple is unchangeable or immutable, to change a tuple we can convert a tuple to a list and then 
# convert the list back to a tuple
tuple_a = ('apple', 'banana', 'lemon')
list_a = list(tuple_a)
list_a[1] = 'strawberry'
tuple_a = tuple(list_a)
print(tuple_a)

# some methods like append(), remove(), insert() that tuple can't have, we have to convert tuple to list to implement it. 
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# unpacking tuple 
# Python allow to extract the value into variable 
(red, yellow, green) = tuple_a
print(red)
print(yellow)
print(green)

tuple_b = ('apple', 'banana', 'lemon','watermelon', 'cucumber')
(red, yellow, *green) = tuple_b
print(red)
print(yellow)
print(green) # return a list when number of values more than variable

# join tuple using operator + 
# method count() index()