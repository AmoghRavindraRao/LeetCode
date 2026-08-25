class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k * (i + 1) in nums:
            i += 1
        
        return k * (i + 1)