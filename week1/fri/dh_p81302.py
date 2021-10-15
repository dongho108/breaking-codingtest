def case_man1(room, i, j):
    # east
    if j + 1 < 5:
        if room[i][j + 1] == 'P':
            return 1

    # south
    if i + 1 < 5:
        if room[i + 1][j] == 'P':
            return 1


def case_man2(room, i, j):
    if i + 1 < 5 and 0 <= j - 1 < 5:
        if room[i + 1][j - 1] == 'P':
            if room[i + 1][j] == 'O' or room[i][j - 1] == 'O':
                return 1
    if i + 1 < 5 and j + 1 < 5:
        if room[i + 1][j + 1] == 'P':
            if room[i + 1][j] == 'O' or room[i][j + 1] == 'O':
                return 1
    if j + 2 < 5:
        if room[i][j + 2] == 'P':
            if room[i][j + 1] == 'O':
                return 1
    if i + 2 < 5:
        if room[i + 2][j] == 'P':
            if room[i + 1][j] == 'O':
                return 1
    return 0


def fuck_corona(room, i, j):
    if case_man1(room, i, j):
        return 1
    if case_man2(room, i, j):
        return 1
    return 0 # 방역수칙 잘 지킴


def solve(place):
    room = []
    for p in place:
        tmp = []
        for i in range(5):
            tmp.append(p[i])
        room.append(tmp)

    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                if fuck_corona(room, i, j):
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(solve(place))
    return answer

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]])) # test case 13
# print(solution([["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]])) # test case 8
