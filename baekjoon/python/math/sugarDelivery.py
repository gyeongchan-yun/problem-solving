'''
    # == 수학 == #
    백준 2839번 설탕 배달

    -n = 3x + 5y, x + y의 최솟 값을 구하여라.
    -정확히 떨어지지 않을 경우 -1을 출력

    예제 입력   예제 출력
    18          4

    해설
    18 = 5 * 3 + 3 * 1 -> 4번

    # 나의 풀이
    큰수를 먼저 놓는것이 유리한 문제!! -> greedy
        -> 단, 이문제의 경우 3과 5로 나누어 져야하는 조건이 있다.
    1. 모든 연산 결과를 두고, min을 결정하는 방식
    2. 3과 5로 나누어 떨어지는지 체크
    3. 아닐경우, 5를 하나 씩 넣으면서 3으로 나누어 지는지 체크
'''


def minimum(num1, num2):
    return num1 if num1 < num2 and num1 != -1 else num2

def main():
    weight = int(input())
    answer = -1

    if weight % 3 == 0:
        answer = int(weight / 3)

    if weight % 5 == 0:
        answer = minimum(answer, int(weight / 5))

    for i in range(1, int(weight / 5) + 1):
        remainder = weight - (5 * i)
        if remainder > 0 and remainder % 3 == 0:
            answer = minimum(answer, int(i + (remainder / 3)))

    print(answer)


if __name__ == "__main__":
    main()