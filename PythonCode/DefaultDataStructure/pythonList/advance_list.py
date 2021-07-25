fruitList = ['apple', 'banana', 'pinapple', 'watermelon']

# for in 
print('Loop by for in')
for fruit in fruitList:
  print(fruit)

print('###')

# loop through index
print('Loop through index')
for i in range(len(fruitList)):
  print(fruitList[i])

print('###')

# while loop 
print('while loop')
i = 0
while i < len(fruitList):
  print(fruitList[i])
  i = i + 1 

print('###')

# loop using list comprehension 
print('loop using list comprehension')
[print(x) for x in fruitList]