'''
    # == BFS == #
    최단경로 문제
    -시작점 과 도착점도 경로의 개수에 포함.
    -(1,1) 부터 (N,M) 까지의 최소경로
    -무조건 도착점이 있는 경우의 입력

    예제 입력   예제 출력
    4 6         15
    101111
    101010
    101011
    111011


    # == 나의 풀이 == #
    1. 갈 수 있는 점을 넣을 수 있는 큐 생성 (처음에 시작점을 넣었음)
    2. main loop: 큐의 길이가 0이 될때까지, 조건: 목표점에 도달하면 break
    3. depth(최소 경로)를 계산 할수 있도록, 큐 사이즈 만큼 loop를 걸고, depth 1씩 추가
        (다른 방법은, 큐에 depth를 같이 넣어주는 방법이 있다.)
    4. 현재 좌표는 dequeue를 통해 얻음
    5. 현재 좌표에서 갈 수 있는 점들을 큐에 넣음 (enqueue)
        조건:
            -한번도 방문하지 않은 점 (visit list를 만들었음)
            -현재 큐에 들어 있지 않는 점
    6. 2번으로 다시 반복
'''


def dequeue(queue):
    return queue.pop(0)


def enqueue(queue, visit, col, row):
    if (col, row) not in queue and (col, row) not in visit:
        queue.append((col, row))
        visit.append((col, row))


def bfs(path):
    # set boundary to prevent out of index error
    min_col, min_row, max_col, max_row = 0, 0, len(path) - 1, len(path[0]) - 1
    depth = 0
    visit = [(0, 0)]
    queue = [(0, 0)]

    while len(queue) != 0:
        for _ in range(0, len(queue)):  # calculate depth
            (col, row) = dequeue(queue)  # current position

            if col == max_col and row == max_row:
                depth += 1
                print(depth)
                return

            if row-1 >= min_row and path[col][row-1] == 1:  # check left position
                enqueue(queue, visit, col, row - 1)

            if row + 1 <= max_row and path[col][row+1] == 1:  # check right position
                enqueue(queue, visit, col, row + 1)

            if col - 1 >= min_col and path[col-1][row] == 1:  # check upper position
                enqueue(queue, visit, col - 1, row)

            if col + 1 <= max_col and path[col+1][row] == 1:  # check down position
                enqueue(queue, visit, col + 1, row)

        depth += 1

    print('depth:', depth)


def main():
    col, row = map(int, input().split())
    path = [list(map(int, input())) for _ in range(0, col)]

    bfs(path)

if __name__ == "__main__":
    main()
