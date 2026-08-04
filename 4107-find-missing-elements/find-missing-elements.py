class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        i, j = nums[0], 0
        while j < n:
            if i == nums[j]:
                i += 1
                j += 1
            else:
                ans.append(i)
                i += 1
        return ans