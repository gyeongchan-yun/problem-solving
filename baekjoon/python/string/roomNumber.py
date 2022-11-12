'''
시간 초과
def main():
    room_num_list = list(map(int, input()))
    one_set = list(range(0,10))

    answer = 0
    while len(room_num_list) != 0:
        answer += 1
        for i in one_set:
            if i == 6:
                if 9 in room_num_list:
                    room_num_list.remove(9)
                    continue
            if i == 9:
                if 6 in room_num_list:
                    room_num_list.remove(6)
                    continue
            if i in room_num_list:
                room_num_list.remove(i)

    print(answer)
'''

def main():
    room_num_list = list(map(int, input()))
    one_set = [0] * 10  # [0, 0, 0, ... 0]
    answer = 0

    if len(room_num_list) != 0:
        answer = 1

    for i in room_num_list:
        if i == 9 and one_set[9] == 1 and one_set[6] != 1:
            one_set[6] = 1
            continue

        if i == 6 and one_set[6] == 1 and one_set[9] != 1:
            one_set[9] = 1
            continue

        if one_set[i] == 0:
            one_set[i] = 1
        else:
            answer +=1
            one_set = [0] * 10
            one_set[i] = 1

    print(answer)


if __name__ == "__main__":
    main()