class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        best = sum(stones)

        for i in list(accumulate(stones))[::-1][1:-1]:
            best = max(best, i - best)
        
        return best
        