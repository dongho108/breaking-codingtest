from bisect import bisect_left, bisect_right


def solution(nums, target):
    if not target in nums:
        return [-1, -1]
    return [bisect_left(nums, target), bisect_right(nums, target) - 1]


print(solution([5,7,7,8,8,10], 8))
print(solution([5,7,7,8,8,10], 6))
print(solution([], 0))