def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = list(set(nums))
    if len(nums) < length:
        answer = len(nums)
    else:
        answer = length
    return answer


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))