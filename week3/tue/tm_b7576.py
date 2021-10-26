from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    result = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
                graph[x][y] = graph[a][b] + 1
                result = graph[a][b]
                queue.append([x, y])
    return result

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

result = bfs()

for i in graph:
    for j in i:
        if j == 0:
            result = -1
            break
    if result == -1:
        break

print(result)