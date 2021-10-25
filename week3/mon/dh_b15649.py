from itertools import permutations

n, m = map(int, input().split())

num = [i + 1 for i in range(n)]
pers = list(permutations(num, m))

for per in pers:
    for i in range(m):
        print(per[i], end=' ')
    print()
