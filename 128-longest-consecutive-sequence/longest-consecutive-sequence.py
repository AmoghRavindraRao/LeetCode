class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        count = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                temp = num

                while temp in nums_set:
                    temp += 1

                count = max(count, temp - num)

        return count
        