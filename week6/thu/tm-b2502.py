import sys


def fibo():
    global D
    f = [1, 1]
    for i in range(2, D-1):
        f.append(f[i-2] + f[i-1])
    return f


if __name__ == "__main__":
    input = sys.stdin.readline
    D, K = map(int, input().strip().split())
    f = fibo()
    print(f)
    a_num = f[D-3]
    b_num = f[D-2]
    print(a_num)
    print(b_num)
    a = 1
    b = 0
    while True:
        val = K - a*a_num
        if val % b_num == 0:
            b = val // b_num
            break
        a += 1
    print(a)
    print(b)
