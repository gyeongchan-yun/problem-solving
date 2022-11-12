'''
    # == DP == #
    Input
        -첫번째 줄 입력은 테스트 케이스의 개수
        -숫자를 입력 할때마다 결과가 출력

    예제 입력   예제 출력
    3
    0           1 0
    1           0 1
    3           1 2
'''


def fibonacci(num, data):
    last_idx = len(data) - 1

    if len(data) != (num + 1):
        for i in range(last_idx + 1, num + 1):
            data.append([(data[i-1][0] + data[i-2][0]), (data[i-1][1] + data[i-2][1])])

    print(data[num][0], data[num][1])


def main():
    num_case = int(input())

    while num_case != 0:
        data = [[1, 0], [0, 1]]

        num = int(input())

        fibonacci(num, data)

        num_case -= 1

if __name__ == "__main__":
    main()
