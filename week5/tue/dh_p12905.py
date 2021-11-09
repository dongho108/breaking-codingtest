def solution(board):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                continue
            cross, left, up = 0, 0, 0
            if 0 < i:
                up = board[i - 1][j]
            if 0 < j:
                left = board[i][j - 1]
            if 0 < i and 0 < j:
                cross = board[i - 1][j - 1]
            board[i][j] = 1 + min(cross, left, up)
            answer = max(answer, board[i][j] * board[i][j])

    return answer