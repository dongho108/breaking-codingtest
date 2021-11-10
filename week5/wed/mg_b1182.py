import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    for item in list(combinations(numbers, i)):
        if sum(item) == S:
            cnt += 1
print(cnt)