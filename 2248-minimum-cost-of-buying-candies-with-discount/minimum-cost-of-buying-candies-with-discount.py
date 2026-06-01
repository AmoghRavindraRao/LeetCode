class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost = sorted(cost)
        count = 0
        amt = 0
        for i in range(len(cost)-1, -1, -1):
            count += 1
            if count % 3 == 0:
                continue
            amt += cost[i]
        return amt