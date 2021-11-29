import sys
from collections import deque
input = sys.stdin.readline
 
def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        x, y = queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt + 1
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
 
for i in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1
 
max_food = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            max_food = max(max_food, bfs(i, j))
print(max_food)