import sys
from collections import deque


input = sys.stdin.readline


def bfs():
    while q:
        x, y, z = q.popleft()
        if not visited[x][y]:
            if x == 0:
                answer.add(z)
            visited[x][y] = True

            if x > 0:
                water = min(b - y, x)
                q.append([x - water, y + water, z])
                water = min(c - z, x)
                q.append([x - water, y, z + water])

            if y > 0:
                water = min(a - x, y)
                q.append([x + water, y - water, z])
                water = min(c - z, y)
                q.append([x, y - water, z + water])

            if z > 0:
                water = min(a - x, z)
                q.append([x + water, y, z - water])
                water = min(b - y, z)
                q.append([x, y + water, z - water])


a, b, c = map(int, input().strip().split())
q = deque()
q.append([0, 0, c])
visited = [[False] * (b + 1) for _ in range(a + 1)]
answer = set()

bfs()

answer = sorted(list(answer))
print(' '.join(map(str, answer)))
