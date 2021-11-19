import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().strip().split())
data = [[0] * m for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    data[a - 1][b - 1] = 1

# print(data)
max_size = 0
visited = [[False] * m for _ in range(n)]
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    size = 1

    while q:
        tx, ty = q.popleft()
        for dx, dy in dir:
            nx = tx + dx
            ny = ty + dy
            if 0 <= nx < n and 0 <= ny < m \
                    and not visited[nx][ny] and data[nx][ny] == 1:
                size += 1
                q.append((nx, ny))
                visited[nx][ny] = True
    return size


for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))

print(max_size)