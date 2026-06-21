class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count = 0
        for i in costs:
            if i <= coins:
                coins -= i
                count += 1
            else:
                break
        return count
        