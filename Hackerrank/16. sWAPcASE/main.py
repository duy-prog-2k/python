# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    result = ''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return result

s = input()
result = swap_case(s)
print(result)

