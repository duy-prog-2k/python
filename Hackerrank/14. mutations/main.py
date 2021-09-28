# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def mutate_string(string, position, character):
    li_string = list(string)
    li_string[position] = character
    result_string = ''.join([str(chara) for chara in li_string]) # chuyen list thanh char
    return result_string
pass

a = mutate_string('xincho', 5, 'a')
print(a)