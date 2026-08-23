
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        winner = 0
        for i in nums:

            if count == 0:
                winner = i
                count = 1
            elif i == winner:
                count += 1
            else:
                count -= 1
        
        return winner