def solution(n):
    answer = []
    combination("", 0, 0, n, answer)
    return answer


def combination(s, open, close, n, answer):
    if len(s) == n * 2:
        answer.append(s)
        return
    if open < n:
        combination(s + '(', open + 1, close, n, answer)
    if close < open:
        combination(s + ')', open, close + 1, n, answer)


print(solution(3))