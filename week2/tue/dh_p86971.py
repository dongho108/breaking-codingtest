from collections import deque


def bfs(x, y, graph):
    queue = deque()
    queue.append(x)
    visited = [0 for i in range(len(graph))]
    visited[y] = 1
    count = 0
    while queue:
        target = queue.popleft()
        visited[target] = 1
        count = count + 1
        for g in graph[target]:
            if not visited[g]:
                queue.append(g)
    return count


def bin_bfs(x, y, graph):
    left = bfs(x, y, graph)
    right = bfs(y, x, graph)

    return abs(left - right)


def solution(n, wires):
    answer = 1e9

    graph = [[] for i in range(n + 1)]

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            temp = bin_bfs(i, graph[i][j], graph)
            if temp < answer:
                answer = temp
    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))