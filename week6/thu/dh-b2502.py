import sys


input = sys.stdin.readline


def day_split(d):
    if d == 0:
        return 1, 0
    elif d == 1:
        return 0, 1
    else:
        a1, b1 = day_split(d - 2)
        a2, b2 = day_split(d - 1)
        return a1 + a2, b1 + b2


def equation(a, b, k):
    i = 1
    while True:
        if (k - (a * i)) % b == 0:
            return i, (k - (a * i)) // b
        i += 1


d, k = map(int, input().split())
a, b = day_split(d - 1)
A, B = equation(a, b, k)
print(A)
print(B)
