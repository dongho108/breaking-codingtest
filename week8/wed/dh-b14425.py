import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, m = map(int, input().strip().split())
word = []
answer = 0
for i in range(n):
    word.append(input().strip())
word.sort()
for j in range(m):
    temp = input().strip()
    if bisect_left(word, temp) != bisect_right(word,temp):
        answer += 1
print(answer)