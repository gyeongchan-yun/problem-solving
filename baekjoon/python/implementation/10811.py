n, m = map(int, input().split())

bucket = [i+1 for i in range(n)]
inputs = [list(map(int, input().split())) for _ in range(m)]

for input in inputs:
    src_idx, dst_idx = input
    temp = bucket[src_idx-1:dst_idx]
    temp.reverse()
    temp_idx = 0
    for i in range(src_idx-1, dst_idx):
        bucket[i] = temp[temp_idx]
        temp_idx += 1

print(' '.join([str(elem) for elem in bucket]))
