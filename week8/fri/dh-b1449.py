import sys
input = sys.stdin.readline

n, l = map(int, input().strip().split())
position = list(map(int, input().strip().split()))

position.sort()

answer = 0
length = 0
for i in range(n):
    if length < position[i]:
        length = position[i] + l - 1
        answer += 1

print(answer)