def solution(nums):
    sets = set()
    for num in nums:
        sets.add(num)
    
    return min(len(nums)//2, len(sets))