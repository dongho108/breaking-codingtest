import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
words = set([input().strip() for _ in range(n)])

result = 0
for _ in range(m):
    word = input().strip()
    if word in words:
        result += 1
print(result)