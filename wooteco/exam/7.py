def wise(map):
    new_map = []
    for i in range(len(map)):
        temp = []
        for j in range(len(map[i])):
            temp.append(map[i][j])
        new_map.append(temp)

    for i in range(len(map)):
        x, y = i, len(map) - 1 - i
        nx, ny = len(map) - 1, 2 * i
        new_map[x][y] = map[nx][ny]

        for j in range(i):
            new_map[x][y+1] = map[nx][ny-1]
            new_map[x][y+2] = map[nx-1][ny-1]
            y += 2
            nx -= 1
            ny -= 1
    return new_map


def counter_wise(map):
    new_map = []
    for i in range(len(map)):
        temp = []
        for j in range(len(map[i])):
            temp.append(map[i][j])
        new_map.append(temp)

    nx, ny = len(map), len(map[0])
    for i in range(len(map)):
        x, y = i, len(map) - 1 - i
        nx, ny = nx - 1, ny - 1
        new_map[x][y] = map[nx][ny]

        tx, ty = nx, ny
        for j in range(i):
            new_map[x][y + 1] = map[tx + 1][ty]
            new_map[x][y + 2] = map[tx + 1][ty - 1]
            y += 2
            tx += 1
            ty -= 1
    return new_map


def solution(grid, clockwise):
    answer = []
    rows = len(grid)
    cols = 2 * (len(grid) - 1) + 1
    new_grid = [['.'] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(len(grid[i])):
            new_grid[i][rows - 1 - i + j] = grid[i][j]

    if clockwise:
        new_grid = wise(new_grid)
    else:
        new_grid = counter_wise(new_grid)

    for i in range(rows):
        temp = ""
        for j in range(cols):
            if new_grid[i][j] != '.':
                temp += new_grid[i][j]
        answer.append(temp)
    return answer


print(solution(["1","234","56789"], True))
print(solution(["1","234","56789"], False))
print(solution(["A","MAN","DRINK","WATER11"], True))
print(solution(["A","MAN","DRINK","WATER11"], False))
print(solution(["A"], True))
print(solution(["A"], False))