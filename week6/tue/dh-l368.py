class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()

        sub_dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sub_dp[i]) < len(sub_dp[j]) + 1:
                    sub_dp[i] = sub_dp[j] + [nums[i]]

        return max(sub_dp, key=len)


test = Solution()
print(test.largestDivisibleSubset([2,3,4,9,8]))
print(test.largestDivisibleSubset(nums=[1]))
print(test.largestDivisibleSubset(nums=[1, 2, 4, 8]))
print(test.largestDivisibleSubset(nums=[1, 2, 3]))