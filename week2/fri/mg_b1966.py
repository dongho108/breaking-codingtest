import sys
from collections import deque
input = sys.stdin.readline

def printer(M, num, importance):
    to_find = num[M]
    printed = []
    while to_find not in printed:
        x = num.popleft()
        y = importance.popleft()
        for imp in importance:
            if y < imp:
                num.append(x)
                importance.append(y)
                break
        else:
            printed.append(x)
    return len(printed)

case = int(input())
for i in range(case):
    N, M = map(int, input().split())
    num = deque(range(N))
    importance = deque(map(int, input().split()))
    print(printer(M, num, importance))
