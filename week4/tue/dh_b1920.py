import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
data = list(map(int, input().split()))

a.sort()
for i in range(m):
    start, end = 0, (n - 1)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < data[i]:
            start = mid + 1
        elif a[mid] > data[i]:
            end = mid - 1
        else:
            answer = 1
            break
    print(answer)