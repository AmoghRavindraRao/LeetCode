class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n= len(nums)
        maxi = nums.index(max(nums))
        mini = nums.index(min(nums))

        left = min(mini, maxi)
        right = max(mini, maxi)

        front = right + 1
        back = n - left

        frontBack = (left + 1) + (n - right)

        return min(front, back, frontBack)
