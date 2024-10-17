N, M = 5, 15
arr = []
for i in range(N):
    col = input()
    arr.append(col)

answer = ''
for j in range(M):
    for i in range(N):
        try:
            answer += arr[i][j]
        except:
            pass
print(answer)