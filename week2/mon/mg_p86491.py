def solution(sizes):
    width, height = 0, 0
    for card in sizes:
        width = max(width, max(card))
        height = max(height, min(card))
    answer = width * height
    return answer