import bisect
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp = arr[:]
        temp = list(dict.fromkeys(temp))
        temp.sort()
        ans = []
        for i in arr:
            index = bisect.bisect_left(temp, i)
            ans.append(index+1)
        return ans