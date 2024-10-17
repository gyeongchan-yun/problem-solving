arr = []
N = 9
max_val = -1
col, row = -1, -1
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            col, row = i, j
print(f'{max_val}\n{col+1} {row+1}')