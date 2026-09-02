class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        left = 0
        total = 0

        for right, number in enumerate(nums):
            total += number

            while total >= target:
                length = min(length, right - left + 1)
                total -= nums[left]
                left += 1

        return length if length != float("inf") else 0