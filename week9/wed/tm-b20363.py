import sys
input = sys.stdin.readline

x, y = map(int, input().strip().split())

print(x+y+min(x,y)//10)
