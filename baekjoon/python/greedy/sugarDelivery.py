def main():
    n = int(input())
    x = int(n / 5)
    answer = -1

    while x >= 0:   # 그리디 방식으로 구현
        remainder = n - (5 * x)
        if remainder % 3 == 0:
            answer = x + int(remainder / 3)
            break   # 맨 처음 나온 결과가 5를 많이 둔 상태로 나온 결과이므로 무조건 최소

        x -= 1

    print(answer)


if __name__ == "__main__":
    main()