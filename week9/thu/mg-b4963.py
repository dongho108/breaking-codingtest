import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def bfs(land, w, h):
    queue = deque()
    cnt = 0
    while land:
        queue.append(land[0])
        while queue:
            x, y = queue.popleft()
            graph[x][y] = 0
            if (x, y) in land:
                land.remove((x, y))
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= h or ny >= w:
                        continue
                    if graph[nx][ny] == 0:
                        continue
                    if graph[nx][ny] == 1:
                        queue.append((nx, ny))
        cnt += 1
    return cnt

while True:
    w, h = map(int, input().split())
    if w * h == 0:
        break
    graph = []
    land = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
        for j in range(w):
            if graph[-1][j] == 1:
                land.append((i, j))
    print(bfs(land, w, h))
