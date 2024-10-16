string = input()

str_len = len(string)
mid_point = str_len // 2 + (str_len % 2)
is_pelindrome = False

for i in range(mid_point):
    if string[i] == string[str_len-1-i]:
        is_pelindrome = True
    else:
        is_pelindrome = False
        break
print(1 if is_pelindrome else 0)