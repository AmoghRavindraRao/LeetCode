class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        if sum(gas) < sum(cost):
            return - 1
        
        amt = 0
        start = 0
        for i in range(n):
            amt += gas[i] - cost[i]
            if amt < 0:
                amt = 0
                start = i + 1
        return start
                

                    

                

        