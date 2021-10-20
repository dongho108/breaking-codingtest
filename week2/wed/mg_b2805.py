import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
start, end = 0, max(array)

def binary_search(arr, target, start, end):
    if start > end:
        return (start + end)//2
    temp = 0
    mid = (start + end)//2
    for i in range(len(arr)):
        if arr[i] - mid < 0:
            continue
        temp += arr[i] - mid
    if temp == target:
        return mid
    if temp < target:
        return binary_search(arr, target, start, mid-1)
    if temp > target:
        return binary_search(arr, target, mid+1, end)

print(binary_search(array, M, start, end))