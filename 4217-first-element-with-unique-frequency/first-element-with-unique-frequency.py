from collections import Counter
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        A = Counter(nums)
        B = Counter(A.values())

        for i in nums:
            if B[A[i]] == 1:
                return i
        return -1
