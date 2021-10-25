import sys


N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
out = []

def solution(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solution(depth+1, N, M)
            visited[i] = False
            out.pop()

solution(0, N, M)