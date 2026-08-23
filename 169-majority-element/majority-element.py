from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(dict(Counter(nums)), key=dict(Counter(nums)).get)