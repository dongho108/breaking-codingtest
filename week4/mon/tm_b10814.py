import sys
import operator

input = sys.stdin.readline

N = int(input())

result = []
for i in range(N):
    age, name = map(str, input().strip().split())
    age = int(age)
    result.append([age, name])

for x, y in sorted(result, key=operator.itemgetter(0)):
    print(f"{x} {y}")