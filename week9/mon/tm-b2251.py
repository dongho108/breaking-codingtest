from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    while q:
        x, y, z = q.popleft()
        if not visit[x][y]:
            visit[x][y] = 1
            if x == 0: 
                answer.append(z)

            if x > 0 and y < b: # a -> b 계획
                water =  min(x, b - y)
                q.append((x-water, y + water, z))
            
            if x > 0 and z < c: # a -> c 계획
                water =  min(x, c - z)
                q.append((x-water, y, z + water))
            
            if y > 0 and x < a: # b -> a 계획
                water =  min(y, a - x)
                q.append((x + water, y - water, z))
            
            if y > 0 and z < c: # b -> c 계획
                water =  min(y, c - z)
                q.append((x, y - water, z + water))

            if z > 0 and y < b: # c -> b 계획
                water =  min(z, b - y)
                q.append((x, y + water, z - water))
            
            if z > 0 and x < a: # c -> a 계획
                water =  min(a - x, z)
                q.append((x + water, y, z - water))
            

a, b, c = map(int, input().split())
visit = [[0] * (b+1) for _ in range(a+1)]
answer = []
q = deque()
q.append([0, 0, c])

bfs()
answer.sort()

print(' '.join(map(str, answer)))