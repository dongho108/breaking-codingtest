def binary_exp(n):
    i = 0
    while n != 1:
        n /= 2
        i += 1
    return i


def fight(a, b, arr, n, x):
    if (a in arr[:n//2] and b in arr[n//2:]) or (a in arr[n//2:] and b in arr[:n//2]):
        return x
    elif a in arr[:n//2]:
        return fight(a, b, arr[:n // 2], n // 2, x - 1)
    else:
        return fight(a, b, arr[n // 2:], n // 2, x - 1)


def solution(n,a,b):
    x = binary_exp(n)
    arr = [i + 1 for i in range(n)]
    return fight(a, b, arr, n, x)

