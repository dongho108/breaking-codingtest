import sys
input = sys.stdin.readline


if __name__ == "__main__":
    string1 = ' ' + input().strip()
    string2 = ' ' + input().strip()
    dp = [[0] * len(string2) for _ in range(len(string1))]
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if string1[i] == string2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    i = len(string1) - 1
    j = len(string2) - 1
    result_string = ""
    
    while dp[i][j]:
        now_dp = dp[i][j]
        if (dp[i-1][j] == now_dp - 1 and dp[i][j-1] == now_dp - 1):
            result_string += string1[i]
            i -= 1
            j -= 1
        elif (dp[i-1][j] == now_dp -1 and dp[i][j-1] == now_dp):
            j -= 1
        else:
            i -= 1

    print(result_string[::-1])