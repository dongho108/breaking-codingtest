import sys
from collections import deque
input = sys.stdin.readline


M, N = map(int, input().split())
box = []
start = []
cnt_zero = 0
for i in range(N):
    box.append(list(map(int, input().split())))
    for j in range(M):
        if box[-1][j] == 1:
            start.append((i, j))
        elif box[-1][j] == 0:
            cnt_zero += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(cnt_zero):
    if cnt_zero == 0:
        return 0
    answer = 0
    queue = deque()
    queue.extend(start)
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
                cnt_zero -= 1
                if box[nx][ny] > answer:
                    answer = box[nx][ny]
    if cnt_zero != 0:
        return -1
    return answer-1

print(bfs(cnt_zero))
