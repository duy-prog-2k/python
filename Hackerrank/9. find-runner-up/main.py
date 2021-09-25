# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
n = int(input())
arr = map(int, input().split())

list_convert = list(arr)
max_of_list = max(list_convert)

filter_max_list = [x for x in list_convert if x != max_of_list] # Lọc thằng lớn nhất ra thì thằng max kế tiếp sẽ là thằng lớn nhì ban đầu
print('The runner up is: ',max(filter_max_list))