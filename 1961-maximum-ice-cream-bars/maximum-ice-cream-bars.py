class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        arr = costs

        max_val = max(arr)
        count = [0] * (max_val + 1)
        
        # Store frequency mapping
        for num in arr:
            count[num] += 1
            
        # Reconstruct the original array in place
        index = 0
        ans = 0
        flag = False
        for num, frequency in enumerate(count):
            for _ in range(frequency):
                arr[index] = num
                index += 1
                if num <= coins:
                    coins -= num
                    ans += 1
                else:
                    flag = True
                    break
            if flag:
                break
        return ans