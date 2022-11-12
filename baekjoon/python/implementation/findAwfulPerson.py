'''
    # == implementation == #
    백준 1764번
    예제 입력           예제 출력
        3 4             2
        ohhenrie       baesangwook
        charlie        ohhenrie
        baesangwook
        obama
        baesangwook
        ohhenrie
        clinton


'''

def main():
    n, m = map(int, input().split())
    h, s = [], []

    for _ in range(0, n):
        h.append(input())

    for _ in range(0, m):
        s.append(input())

    ans = list(set(h).intersection(set(s)))
    ans.sort()

    print(len(ans))
    print('\n'.join(ans))

if __name__ == "__main__":
    main()