import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n + m):
    data.append(list(map(int, input().split())))

road = []
yj = []

for i in range(n):
    length, speed = data[i]
    road += [speed] * length

for i in range(n, n + m):
    length, speed = data[i]
    yj += [speed] * length

answer = 0
for i in range(100):
    answer = max(answer, yj[i] - road[i])
print(answer)