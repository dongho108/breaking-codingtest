import sys
input = sys.stdin.readline

N, M = map(int, input().split())

velocity = []
for _ in range(N):
    a, b = map(int, input().split())
    velocity.extend([b] * a)

drive = []
for _ in range(M):
    c, d = map(int, input().split())
    drive.extend([d] * c)

ans = 0
for i in range(100):
    ans = max(ans, drive[i]-velocity[i])

print(ans)