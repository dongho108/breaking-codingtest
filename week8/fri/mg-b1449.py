import sys
input = sys.stdin.readline

N, L = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

i, cnt = 0, 0
while i < len(loc)-1:
    j = 1
    while loc[i+j] - loc[i] <= L-1:
        j += 1
        if i+j >= len(loc):
            break
    cnt += 1
    i += j
    if i == len(loc)-1:
        cnt += 1
        break

if cnt == 0:
    cnt += 1

print(cnt)
