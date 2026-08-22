class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                n -= 1
                continue
            i += 1
        return n
        