from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    
    result = []
    count = [bridge_length for _ in range(len(truck_weights))]
    index = -1
    while queue:
        answer += 1
        q = queue.popleft()
        weights = 0
        if result != [] and count[result[0][1]] == 1:
            result.remove(result[0])
        
        for i,j in result:
            weights += i
            count[j] -= 1
        
        if weights + q <= weight:
            index += 1
            result.append((q,index))
        else:
            queue.appendleft(q)
        
    answer += bridge_length
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))