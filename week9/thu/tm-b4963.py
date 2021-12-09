import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    dx = [1,-1,0,0,1,-1,1,-1]
    dy = [0,0,1,-1,1,1,-1,-1]

    graph[i][j] = 0
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

while True:
    w, h = map(int,input().strip().split())
    
    if w == 0 and h == 0 :
        break

    graph = [list(map(int,input().strip().split())) for _ in range(h)]
    
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1

    print(count)