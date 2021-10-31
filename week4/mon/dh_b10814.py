import sys

input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    age, name = map(str, input().split())
    data.append((int(age), i, name))

data.sort(key=lambda x:(x[0], x[1]))
for i in range(n):
    print(data[i][0], data[i][2])
