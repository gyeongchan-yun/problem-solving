n, m = map(int, input().split())

bucket = [0 for _ in range(n)]
inputs = [list(map(int, input().split())) for _ in range(m)]

for input in inputs:
    first_bucket_idx, sec_bucket_idx, ball_number = input
    for i in range(first_bucket_idx, sec_bucket_idx+1):
        bucket[i-1] = ball_number

print(' '.join([str(elem) for elem in bucket]))