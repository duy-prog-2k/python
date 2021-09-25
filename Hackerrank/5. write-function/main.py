# https://www.hackerrank.com/challenges/write-a-function/problem
def leap(year):
    if(year % 100 == 0):
        if(year % 400 == 0):
            return True
        else:
            return False
    elif(year % 4 == 0):
        return True
    else:
        return False

year = int(input())
print(leap(year))