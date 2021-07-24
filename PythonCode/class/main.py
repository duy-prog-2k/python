class Fruit:

  # constructor
  def __init__(self, name, color):
    self.name = name
    self.color = color
  
  def greeting(self):
    print("Hello, I'm", self.name, "I'm", self.color)
pass 

banana = Fruit('Banana', 'yellow') # create new object

banana.greeting()

# class Apple(Fruit):
#   def __init__(self, name, color)
