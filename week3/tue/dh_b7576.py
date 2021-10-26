import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(input().split()))

answer = 0

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == "1":
            queue.append((0, 1, i, j))

dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
while queue:
    day, target, x, y = queue.popleft()
    if answer < day:
        answer = day
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == "0":
                queue.append((day + 1, target, nx, ny))
                box[nx][ny] = "1"

for i in range(n):
    for j in range(m):
        if box[i][j] == "0":
            answer = -1
            break
    if answer == -1:
        break
print(answer)