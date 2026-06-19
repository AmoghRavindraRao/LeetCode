class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        tot = 0
        high = float("inf") * -1
        for i in gain:
            tot += i
            high = max(high, tot)
        if high <= 0:
            return 0
        else:
            return high