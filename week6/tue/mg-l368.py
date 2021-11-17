class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        temp = {}
        for i in range(len(nums)):
            temp[nums[i]] = [nums[i]]
            for item in sorted(temp.items(), key=lambda x:-len(x[1])):
                if nums[i] == item[0]:
                    continue
                if nums[i] % item[0] == 0:
                    temp[nums[i]].extend(temp[item[0]])
                    break
            if len(temp[nums[i]]) > len(answer):
                answer = temp[nums[i]]
        return answer