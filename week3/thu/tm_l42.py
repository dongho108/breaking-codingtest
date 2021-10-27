class Solution:
    def trap(self, height: list[int]) -> int:
        
        len_height = len(height)
        high_left, high_right = [0] * len_height, [0] * len_height
        
        for i in range(1,len_height-1):
            high_left[i] = max(high_left[i-1], height[i-1])
            high_right[len_height-i-1] = max(high_right[len_height-i], height[len_height-i])
        
        water = 0
        for i in range(len_height):
            water += max(min(high_left[i], high_right[i])-height[i], 0)
        
        return water

print(Solution().trap([4,2,0,3,2,5]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))