# https://www.hackerrank.com/challenges/nested-list/problem
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = [x[1] for x in students]
min_score = min(scores)

students_filter = [x for x in students if x[1] != min_score]

scores = [x[1] for x in students_filter]
min_2nd_score = min(scores)
min_2nd = [x for x in students_filter if x[1] == min_2nd_score]
for x in min_2nd.sort():
    print(x[0])

# f __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     scores = [x[1] for x in students]
#     min_score = min(scores)

#     students_filter = [x for x in students if x[1] != min_score]

#     scores = [x[1] for x in students_filter]
#     min_2nd_score = min(scores)
#     min_2nd = [x for x in students_filter if x[1] == min_2nd_score]
#     name = [x[0] for x in min_2nd]
#     name.sort()
#     for x in name:
#         print(x)