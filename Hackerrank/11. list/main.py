# https://www.hackerrank.com/challenges/python-lists/problem 
N = int(input())
actions = []
result = [] 
for i in range(N):
    actions.append(input().split())

for action in actions:
    if action[0] == 'append':
        result.append(int(action[1]))
    elif action[0] == 'insert':
        result.insert(int(action[1]), int(action[2]))
    elif action[0] == 'print':
        print(result)
    elif action[0] == 'remove':
        result.remove(int(action[1]))
    elif action[0] == 'sort':
        result.sort()
    elif action[0] == 'pop':
        result.pop();
    elif action[0] == 'reverse':
        result.reverse()


