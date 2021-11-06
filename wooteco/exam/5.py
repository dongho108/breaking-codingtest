def zero_check(answer):
    for i in range(len(answer)):
        if 0 in answer[i]:
            return True
    return False


def solution(rows, columns):
    answer = [[0] * columns for _ in range(rows)]

    now_x = 0
    now_y = 0
    now = 1
    dir = 0  # 아래로 (x + 1)
    dir_arr = [[-1] * columns for _ in range(rows)]
    while zero_check(answer):
        if answer[now_x][now_y] != 0 and dir == dir_arr[now_x][now_y]:
            break
        answer[now_x][now_y] = now
        dir_arr[now_x][now_y] = dir
        if now % 2 == 0:
            now_x = (now_x + 1) % rows
            dir = 0
        else:
            now_y = (now_y + 1) % columns
            dir = 1
        now += 1

    return answer


# for i in range(2, 100):
#     for j in range(2, 100):
#         print(i, j)
#         solution(i, j)
# print(solution(2, 3))
# print(solution(2, 2))
# print(solution(3, 4))
# print(solution(3, 3))