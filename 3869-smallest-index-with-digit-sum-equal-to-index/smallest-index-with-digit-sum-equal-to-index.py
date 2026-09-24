class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            n = nums[i]
            s = 0
            while n:
                s += n % 10
                n = n // 10
            
            if i == s:
                return i
        
        return -1
        