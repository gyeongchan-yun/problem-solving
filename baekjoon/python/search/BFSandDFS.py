'''
    # == DFS 와 BFS 경로 탐색 비교하기 == #
    Input
        -첫째줄 입력은, 각각 vertex 개수, edge 개수, 시작 노드를 의미한다.
        -간선은 양방향
        -(시작 노드) (끝 노드)

    Output
        -첫번째 줄은 DFS
        -두번째 줄은 BFS

    예제 입력   예제 출력
    4 5 1       1 2 4 3
    1 4         1 2 3 4
    1 2
    1 3
    2 4
    3 4
'''


def dequeue(queue):
    return queue.pop(0)


def enqueue(queue, visit, node):
    if node not in queue and node not in visit:
        queue.append(node)
        visit.append(node)


def dfs(path, visit, node):
    if node in visit:
        return

    visit.append(node)

    for next_node in path[node]:
        dfs(path, visit, next_node)


def bfs(path, start_node):
    visit = [start_node]
    queue = [start_node]

    while len(queue) != 0:
        cur_node = dequeue(queue)  # current node

        for node in path[cur_node]:
            enqueue(queue, visit, node)

    print(' '.join(list(map(str, visit))))


def main():
    num_vertex, num_edge, start_node = map(int, input().split())

    # path 딕셔너리로 구현.
    path = {}
    for _ in range(0, num_edge):
        start, end = map(int, input().split())

        if start not in path.keys():
            path[start] = []

        if end not in path.keys():
            path[end] = []

        path[start].append(end)
        path[end].append(start)

    for k, v in path.items():
        v.sort()

    visit = []

    dfs(path, visit, start_node)
    print(' '.join(map(str, visit)))

    bfs(path, start_node)


if __name__ == "__main__":
    main()