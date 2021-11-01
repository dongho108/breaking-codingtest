import sys
input = sys.stdin.readline


N = int(input())
info = []
for i in range(N):
    temp = input().split()
    temp.append(i)
    info.append(temp)
info = sorted(info, key=lambda x:(int(x[0]), x[2]))

for ans in info:
    print(ans[0], ans[1])