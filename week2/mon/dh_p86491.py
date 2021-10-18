def swap(x, y):
    return y, x


def solution(sizes):
    height = []
    width = []

    for size in sizes:
        height.append(size[0])
        width.append(size[1])

    for i in range(len(height)):
        if height[i] < width[i]:
            height[i], width[i] = swap(height[i], width[i])

    return max(height) * max(width)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))