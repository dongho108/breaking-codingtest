# from itertools import permutations
#
# n, m = map(int, input().split())
#
# num = [i + 1 for i in range(n)]
# pers = list(permutations(num, m))
#
# for per in pers:
#     for i in range(m):
#         print(per[i], end=' ')
#     print()

n, m = map(int, input().split())

num = [i + 1 for i in range(n)]
visited = [False for _ in range(n + 1)]
results = []


def backtracking(depth):
    if depth == m:
        print(' '.join(map(str, results)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            results.append(i)
            backtracking(depth + 1)
            visited[i] = False
            results.pop()


backtracking(0)
