'''
    # == 문자열 처리 == #
    백준 10809 알파벳 찾기
    예제 입력
    baekjoon

    예제 출력
    1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

    # 나의 풀이
    1. 아스키 코드를 이용하여 알파벳 리스트를 만듬 (소문자)
    2. 알파벳 리스트를 일일이 체크하여, find() 함수를 이용하여 index 추출
'''


def main():
    sentence = input()

    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    ans = []

    for char in alphabets:
        ans.append(sentence.find(char))

    print(' '.join(list(map(str, ans))))

if __name__ == "__main__":
    main()
