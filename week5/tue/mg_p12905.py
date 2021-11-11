def solution(board):
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue
            
            if i == 0 or j == 0:
                dp[i][j] = board[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            
            if dp[i][j] > answer:
                answer = dp[i][j]
    return answer**2
