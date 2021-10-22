from collections import deque

cases = int(input())
for case in range(cases):
    n, m = map(int, input().split())
    answer = 0

    temp = list(map(int, input().split()))
    queue = deque()
    for i in range(len(temp)):
        queue.append([i, temp[i]])

    while True:
        inx, x = queue.popleft()
        check = False
        for i in range(len(queue)):
            if x < queue[i][1]:
                queue.append([inx, x])
                check = True
                break
        if not check:
            answer += 1
            if m == inx:
                break
    print(answer)

