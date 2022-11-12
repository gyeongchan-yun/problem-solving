'''
    # == for 문 활용하기 == #
    예제 입력   예제 출력
    5               *
                   **
                  ***
                 ****
                *****
'''


def print_star(num):
    star = '*'
    for i in range(1, num + 1):
        stars = star * i
        print(stars.rjust(num))


def main():
    num = int(input())

    print_star(num)

if __name__ == "__main__":
    main()
