# lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

x = lambda a:a+10 

print(x(5))

multi = lambda a,b : a * b

print(multi(2,10))

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for j in range(1, i+1): print(i, end='') 
    print('')