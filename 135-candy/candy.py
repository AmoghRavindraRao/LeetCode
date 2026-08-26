class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cost = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                cost[i] = cost[i - 1] + 1
        candy = 0
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                cost[i - 1] = max(cost[i] + 1, cost[i - 1])
            
            candy += cost[i - 1]
        
        return candy + cost[n - 1]