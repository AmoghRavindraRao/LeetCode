class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        n = len(nums)
        while i < n:
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.pop(i)
                n -= 1
                continue
            i += 1


        