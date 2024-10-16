N, M = map(int, input().split())
A, B = [], []
for i in range(2*N):
    elem = map(int, input().split())
    if len(A) < N:
        A.append(elem)
    else:
        B.append(elem)

for a_col, b_col in zip(A, B):
    c_col = []
    for a, b in zip(a_col, b_col):
        c_col.append(a + b)
    print(' '.join([str(c) for c in c_col]))