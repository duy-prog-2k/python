fruits = ['apple', 'pinapple', 'banana', 'kiwi', 'cherry']

# syntax for list comprehension: newlist = [expression for item in iterable if condition == True]

new_fruit = [x for x in fruits if 'a' in x]

print(new_fruit)