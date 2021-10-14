x = int(input())

dp = [0 for i in range(x + 1)]

for i in range(2, x + 1):
    case1 = x
    case2 = x
    case3 = x

    if i % 3 == 0:
        case1 = dp[int(i / 3)]
    if i % 2 == 0:
        case2 = dp[int(i / 2)]
    case3 = dp[i - 1]
    dp[i] = min(case1, case2, case3) + 1

print(dp[x])
