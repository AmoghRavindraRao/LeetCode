class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2: return n
        bits = n.bit_length() - 1
        return 1 << (bits+1)