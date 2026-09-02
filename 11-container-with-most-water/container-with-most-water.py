class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        count = n - 1
        result = 0
        while i < j:
            result = max(result, (min(height[i], height[j]) * count))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            count -= 1
        
        return result
