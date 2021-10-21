import sys
from collections import deque
input = sys.stdin.readline
    
def making_list(importance):
    queue = deque([])
    for index, score in enumerate(importance):
        queue.append((score,index))
    return queue

for _ in range(int(input())):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = making_list(importance)
    order = 0
    max_score = max(importance)
    while queue:
        score, index = queue.popleft()
        if score == max_score:
            if index == m:
                break
            max_score = max(queue)[0]
            order += 1
        else:
            queue.append((score, index))
    print(order+1)