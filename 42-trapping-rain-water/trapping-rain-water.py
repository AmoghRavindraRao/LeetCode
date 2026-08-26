class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        left = height[start]
        right = height[end]
        water = 0

        while start < end:
            if left < right:
                start += 1
                left = max(left, height[start])
                water += left - height[start]
            
            else:
                end -= 1
                right = max(right, height[end])
                water += right - height[end]
        
        return water

        