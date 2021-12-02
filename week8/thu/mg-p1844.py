from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maps):
    N, M = len(maps), len(maps[0])
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[N-1][M-1]
    
def solution(maps):
    answer = bfs(maps)
    if answer == 1:
        if len(maps) == 2 and len(maps[0]) == 1:
            return 1
        elif len(maps) == 1 and len(maps[0]) == 2:
            return 1         
        return -1
    return answer