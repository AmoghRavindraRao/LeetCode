class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left = []
        right = []
        middle = []
        for i in nums:
            if i < pivot:
                left.append(i)
            if i > pivot:
                right.append(i)
            if i == pivot:
                middle.append(i)
        return left + middle + right