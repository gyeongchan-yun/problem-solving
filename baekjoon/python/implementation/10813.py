n, m = map(int, input().split())

bucket = [i+1 for i in range(n)]
inputs = [list(map(int, input().split())) for _ in range(m)]

for input in inputs:
    src_idx, dst_idx = input
    temp = bucket[dst_idx-1]
    bucket[dst_idx-1] = bucket[src_idx-1]
    bucket[src_idx-1] = temp

print(' '.join([str(elem) for elem in bucket]))

