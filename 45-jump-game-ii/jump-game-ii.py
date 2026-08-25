class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        far = near = jumps = 0
        
        while far < n - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            near += 1
            far = farthest
            jumps += 1
        
        return jumps

