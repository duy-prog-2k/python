# https://www.hackerrank.com/challenges/find-a-string/problem
# Ý tưởng của tui là tui sẽ cắt cái list bằng với substring đối với mỗi từ trong list
# Sau só tui sẽ so sánh những cái list đã được slide đó với substring, nếu bằng thì count + 1
a = 'ABCDCDC'
count = 0
for i in range(0, len(a)):
    sub_string = a[i:i+len('CDC')]
    if sub_string ==  'CDC':
        count = count + 1
print(count)

