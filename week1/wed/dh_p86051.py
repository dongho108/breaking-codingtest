def solution(numbers):
    digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    answer = 0
    for d in digit:
        if d not in numbers:
            answer += d
    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))