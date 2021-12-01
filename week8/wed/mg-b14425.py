import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input().strip())

cnt = 0
for j in range(M):
    check = input().strip()
    if check in S:
        cnt += 1
print(cnt)