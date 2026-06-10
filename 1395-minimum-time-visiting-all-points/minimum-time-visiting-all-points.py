class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        cost = 0
        if n == 1:
            return 0
        for i in range(n - 1):
            x = abs(points[i + 1][0] - points[i][0])
            y = abs(points[i + 1][1] - points[i][1])
            if x >= y:
                cost += x
            else:
                cost += y
        
        return cost

            
            

