def get_meet(a, b):
    if (a[0] * b[1] - a[1] * b[0]) == 0:
        return
    x = (a[1] * b[2] - a[2] * b[1]) / (a[0] * b[1] - a[1] * b[0])
    y = (a[2] * b[0] - a[0] * b[2]) / (a[0] * b[1] - a[1] * b[0])
    if (x - int(x) == 0) and (y - int(y) == 0):
        return [int(x), int(y)]


def solution(line):
    answer = []

    meets = []
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            temp = get_meet(line[i], line[j])
            if temp:
                meets.append(temp)

    i_start, j_start = 1e15, 1e15
    i_end, j_end = -1e9, -1e9

    for meet in meets:
        if meet[0] < i_start:
            i_start = meet[0]
        if meet[1] < j_start:
            j_start = meet[1]
        if i_end < meet[0]:
            i_end = meet[0]
        if j_end < meet[1]:
            j_end = meet[1]

    for j in range(j_end, j_start - 1, -1):
        temp = []
        for i in range(i_start, i_end + 1):
            if [i, j] in meets:
                temp.append("*")
            else:
                temp.append(".")
        answer.append("".join(temp))

    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
