import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
start, end = 0, max(array)

def binary_search(arr, target, start, end, total):
    temp = 0
    mid = (start + end)//2
    for i in range(len(arr)):
        if arr[i] - mid < 0:
            continue
        temp += arr[i] - mid
    if temp == target:
        return mid
    if temp < target:
        return binary_search(arr, target, start, mid-1, temp)
    # if temp > target: 여기가 문제


print(binary_search(array, M, start, end, 1e9))
