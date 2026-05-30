from collections import Counter
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for i in nums:
            if i in data:
                data[i] +=1
            else:
                data[i] = 1
        return max(data, key=data.get)
        