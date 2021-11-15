import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    Rout = 0
    Cout = 0
    R_n = n
    C_n = n
    R = [False for _ in range(n+1)]
    C = [False for _ in range(n+1)]
    s = (n * (n+1)) // 2
    for _ in range(q):
        line, num = map(str, input().strip().split())
        num = int(num)
        result = 0
        if line == "R":
            if R[num] == False:
                result += s + R_n * num - Cout
                C_n -= 1
                Rout += num
                R[num] = True
                R.append(num)
        else:
            if C[num] == False:
                result += s + C_n * num - Rout
                R_n -= 1
                Cout += num
                C[num] = True
                C.append(num)
        print(result)
