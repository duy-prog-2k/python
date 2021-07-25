''' Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is both unordered and unindexed.
Sets are written with curly brackets.'''
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Duplicate is not allowed 
# Can't change the items after the set has been created but can add new item
# get length like list and tuple
# access using for loop 
set_a = {'apple', 'banana', 'orange'}

# add item using add method
set_a.add('lemon')

# add item from another iterable like list, set
set_b = {'Pham', 'Khac', 'Duy'}
set_a.update(set_b)

list_test = [1, 2, 4]
set_a.update(list_test)
print(set_a)

# remove item using remove or discard 
# remove lemon using remove 
set_a.remove('lemon') # if the item to delete doesn't exists, remove() will raise an error
set_a.discard('lemon') # if the item to delete doesn't exists, discard() will not raise an error
print(set_a)

# can using pop to delete item but pop() method will remove the last item, we can't know which items that get removed
# join set using union() method