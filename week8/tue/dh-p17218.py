import sys


input = sys.stdin.readline
a = input().strip()
b = input().strip()


str1 = "0" + a
str2 = "0" + b
dp = [[0] * len(str1) for _ in range(len(str2))]

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str1[j] == str2[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


def print_dp(x, y):
    if x == 0 and y == 0:
        return
    if str1[x] == str2[y]:
        print_dp(x - 1, y - 1)
        print(str1[x], end='')
    else:
        if dp[y - 1][x] == dp[y][x] and 0 <= y - 1:
            print_dp(x, y - 1)
        else:
            print_dp(x - 1, y)


print_dp(len(str1) - 1, len(str2) - 1)

