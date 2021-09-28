# https://www.hackerrank.com/challenges/find-a-string/problem
a = 'ABCDCDC'
count = 0
for i in range(0, len(a)):
    sub_string = a[i:i+len('CDC')]
    if sub_string ==  'CDC':
        count = count + 1
print(count)

