from collections import deque

cases = int(input())
for case in range(cases):
    n, m = map(int, input().split())
    answer = 0

    temp = list(map(int, input().split()))
    queue = deque()
    for i, t in enumerate(temp):
        queue.append((t, i))
    max_value = max(queue)[0]
    while True:
        imp, inx = queue.popleft()
        if max_value == imp:
            answer += 1
            if m == inx:
                break
            max_value = max(queue)[0]
        else:
            queue.append((imp, inx))
    print(answer)

