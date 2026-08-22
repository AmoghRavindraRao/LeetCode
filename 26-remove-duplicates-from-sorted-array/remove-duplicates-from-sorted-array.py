class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        i = 0
        while i < n:
            if nums[i] not in s:
                s.add(nums[i])
                i += 1
            elif nums[i] in s:
                nums.pop(i)
                n -= 1
                continue
        return n
        