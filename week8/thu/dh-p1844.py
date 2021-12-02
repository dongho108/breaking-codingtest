from collections import deque


def solution(maps):
    answer = -1
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    queue = deque()
    queue.append((0, 0))

    distance = [[-1] * len(maps[0]) for _ in range(len(maps))]
    distance[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            answer = distance[x][y]
            break
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                if distance[nx][ny] == -1:
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1

    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))