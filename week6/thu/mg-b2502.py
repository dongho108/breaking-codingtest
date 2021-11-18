import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 2
i, temp_idx = 1, 1
temp_B = B
while i != B-1:
    cnt += 1
    bef = temp_B-temp_idx
    if cnt == A and bef >= temp_idx >= 1:
        print(temp_idx)
        print(bef)
        break
    if bef < 1 or temp_idx < 1 or temp_idx > bef:
        i += 1
        temp_B, temp_idx = B, i
        cnt = 2
        continue
    temp_B = bef
    temp_idx = bef-temp_idx
