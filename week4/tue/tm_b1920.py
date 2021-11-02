from bisect import bisect_left
import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    a = sorted(list(map(int, input().strip().split())))
    m = int(input())
    for i in map(int, input().strip().split()):
        if a[bisect_left(a, i) % n] != i:
            print(0)
        else:
            print(1)
