from collections import deque

def solution(people, limit):
    
    people.sort()
    answer = 0
    q = deque([(0,len(people)-1)])
    while q:
        answer += 1
        first, end = q.pop()
        if people[first] + people[end] <= limit:
            first += 1
        end -= 1
        if first < end:
            q.append((first,end))
        elif first == end:
            answer += 1
    return answer