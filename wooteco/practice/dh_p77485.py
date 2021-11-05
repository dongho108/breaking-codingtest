def rotation(arr, query):
    min_value = 1e9
    x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
    new_arr = [item[:] for item in arr]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_inx = -1

    now_x = x1
    now_y = y1
    while True:
        if (now_x == x1 or now_x == x2) and (now_y == y1 or now_y == y2):
            dir_inx += 1
        dir_x = dir[dir_inx][0]
        dir_y = dir[dir_inx][1]
        new_arr[now_x + dir_x][now_y + dir_y] = arr[now_x][now_y]
        min_value = min(min_value, arr[now_x][now_y])
        if now_x + dir_x == x1 and now_y + dir_y == y1:
            break
        now_x += dir_x
        now_y += dir_y
    return new_arr, min_value


def solution(rows, columns, queries):
    answer = []

    arr = []
    data = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(data)
            data += 1
        arr.append(temp)

    for query in queries:
        arr, min_value = rotation(arr, query)
        answer.append(min_value)

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
