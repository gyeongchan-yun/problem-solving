N = int(input())

# my answer
star = '*'
for i in range(N):
    input = ' ' * (N-1-i)
    print(input + star * (2*i+1))
for i in range(N-2, -1, -1):
    input = ' ' * (N-1-i)
    print(input + star * (2*i+1))


# Good answer: https://jinho-study.tistory.com/86
"""
n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
"""