def solution(arr):
    answer = []
    data = []
    for i in range(3):
        data.append(arr.count(i+1))

    max_value = max(data)
    for i in range(3):
        answer.append(max_value - data[i])
    return answer

print(solution([2, 1, 3, 1, 2, 1]))