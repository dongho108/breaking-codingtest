import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
M = int(input())

for i in list(map(int, input().split())):
    if i in graph:
        print(1)
    else:
        print(0)