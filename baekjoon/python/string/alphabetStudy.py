'''
    # == 문자열 처리 == #
    백준 1157 단어 공부
    조건:
    1. 알파벳 대소문자로 된 단어에서, 가장 많이 쓰인 단어를 찾아 대문자로 출력
    2. 대소문자를 구분하지 않는다.

    예제 입력
    zZa

    예제 출력
    Z

    # 나의 풀이 & 방법
    1. 자료형 set 은 중복을 허용하지 않음.
    2. string -> list: list(string)
       list -> string: ''.join(list)
    3. string 함수
        count(char)
        lower()
        upper()
        split() -> parameter 없으면 공백을 기준으로

'''

def main():
    word = input()

    alphabet_list = list(set(list(word))) # set 은 중복된 값 허용 X
    alphabet_dict = {}

    for char in alphabet_list:
        num = word.count(char)
        if char.lower() in alphabet_dict.keys():
            alphabet_dict[char.lower()] += num
        else:
            alphabet_dict[char.lower()] = num

    answer = [key for key, val in alphabet_dict.items() if val == max(alphabet_dict.values())]

    if len(answer) > 1:
        print('?')
    else:
        print(answer[0].upper())

if __name__ == "__main__":
    main()