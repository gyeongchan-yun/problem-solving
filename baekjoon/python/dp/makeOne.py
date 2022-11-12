'''
    # == DP == #
    1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    2. X가 2로 나누어 떨어지면, 2로 나눈다.
    3. 1을 뺀다.
    X를 1로 만들 수 있는 최소연산의 개수

    예제 입력   예제 출력
    2           1
    10          3

    부가 설명:
        10은 (10 -> 9 -> 3 -> 1) 3번의 연산으로 1이 될 수 있다.


    # == 나의 풀이 == #
    1. 결과 값을 저장 할 array 생성.
        index에 매칭되는 숫자들의 value는 최소연산의 개수(결과값)
            ex) arr[3] -> 3이 1이 될 수 있는 최소 연산 개수
    2. 점화식 활용 (주석 참고)
'''


def min(num1, num2):
    return num1 if num1 < num2 else num2


def make_one(number, arr):
    for i in range(2, number + 1):
        res = arr[i-1] + 1  # Tn = Tn-1 + 1 (default: 1을 빼는 연산이므로, 연산 개수는 1이 더해짐)

        if i % 2 == 0:
            res = min(res, arr[int(i/2)] + 1)  # Tn = min( Tn-1 + 1, Tn/2 + 1): 2로 나누는 연산으로, 1이 더해짐

        if i % 3 == 0:
            res = min(res, arr[int(i/3)] + 1)  # Tn = min( Tn-1 + 1, Tn/3 + 1): 3으로 나누는 연산으로, 1이 더해짐

        arr.append(res)

    print(arr[number])


def main():
    num = int(input())
    dp_arr = [-1, 0]  # To sync number and index

    make_one(num, dp_arr)


if __name__ == "__main__":
    main()
