from bisect import bisect_left, bisect_right


class Solution1:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if nums == []:
            return [-1, -1]
        first_index = bisect_left(nums, target) % len(nums)
        if nums[first_index] != target:
            return [-1, -1]

        result = [first_index]
        first_index += 1
        first_index %= len(nums)

        while True:
            if first_index == 0:
                result.append(len(nums)-1)
                break
            elif nums[first_index] != target:
                result.append(first_index-1)
                break
            first_index += 1
            first_index %= len(nums)

        return result


test = Solution1()
print(test.searchRange(nums=[], target=0))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))


class Solution2:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if nums == []:
            return [-1, -1]
        first_index = bisect_left(nums, target) % len(nums)
        if nums[first_index] != target:
            return [-1, -1]
        last_index = bisect_right(nums, target)
        result = [first_index, last_index-1]

        return result


test = Solution2()
print(test.searchRange(nums=[], target=0))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
