a = int(input())

b = (a // 4)
answer_postfix = 'int'
answer_prefix = 'long '
answer = ''
for i in range(b):
    answer += answer_prefix
answer += answer_postfix

print(answer)