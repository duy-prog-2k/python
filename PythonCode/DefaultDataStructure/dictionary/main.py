'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
'''
thisdict = {
  'brand': 'Ford',
  'model': 'mustang',
  'year': 1964
}

print(thisdict)

# Access this dict
print(thisdict['brand'])
print(thisdict.get('model'))

# Get a list of key
print(thisdict.keys())

# Change or add dict item 
# use one of these way, if the item doesn't exists, it will be added to this dict  
thisdict['year'] = 1965

thisdict.update({'model': 'Ranger'})

print(thisdict)

# remove item 
thisdict.pop('year') # argument is key of the item that we want to delete 
# thisdict.popitem() will delete the last item in this dict

# forloop
# print key 
for x in thisdict:
  print(x)

# print value 
# or 
# for x in thisdict.values():
#   print(x)
for x in thisdict:
  print(thisdict[x])

# loop through both key and value 
for x, y in thisdict.items():
  print(x +':', y)

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
dict_clone1 = thisdict.copy()

# Another way to make a copy is to use the built-in function dict().
dict_clone2 = dict(thisdict)

# nested dict 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)