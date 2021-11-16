class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        
        nums = sorted(nums)
        
        len_subset = [1] * len(nums)
        last_index = [-1] * len(nums)

        max_len_subset = 0
        max_index = -1
        for idx1, num in enumerate(nums):
            for idx2 in range(idx1-1,-1,-1):
                if num % nums[idx2] == 0 :
                    if len_subset[idx2] + 1 > len_subset[idx1]:
                        len_subset[idx1] = len_subset[idx2] + 1
                        last_index[idx1] = idx2
                        
            if max_len_subset < len_subset[idx1]:
                max_len_subset = len_subset[idx1]
                max_index = idx1
            
        answer = []    
        while max_index >= 0:
            answer.insert(0,nums[max_index])
            max_index = last_index[max_index]
        
        return answer

test = Solution()
print(test.largestDivisibleSubset(nums = [1,2,4,8]))
print(test.largestDivisibleSubset(nums = [1,2,3]))
