def greeting(name):
  print('Hello ' + name);

greeting('Duy')

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def greeting(*name):
  print('Hello ' + name[2])

greeting('Duy', 'Khang', 'Van')

