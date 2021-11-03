class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        
        n = len(nums)
        if n % 2 == 1:
            answer = nums[n // 2]
        else:
            answer = (nums[n // 2 - 1] + nums[n // 2]) / 2.0
            
        return answer