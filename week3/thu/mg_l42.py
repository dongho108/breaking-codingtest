class Solution:
    def trap(self, height: List[int]) -> int:
        
        len_height = len(height)
        high_left, high_right = [0] * len_height, [0] * len_height
        
        for i in range(1,len_height-1):
            high_left[i] = max(high_left[i-1], height[i-1])
            high_right[len_height-i-1] = max(high_right[len_height-i], height[len_height-i])
        
        water = 0
        for i in range(len_height):
            water += max(min(high_left[i], high_right[i])-height[i], 0)
        
        return water