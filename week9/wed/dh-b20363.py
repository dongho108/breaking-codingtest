import sys

input = sys.stdin.readline


x, y = map(int, input().strip().split())
print(x + min(x, y)//10 + y)
