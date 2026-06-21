class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        def counting_sort(arr):
            if not arr:
                return arr
                
            # Find the range of the input data
            max_val = max(arr)
            range_val = max_val + 1
            
            # Initialize count and output arrays
            count = [0] * range_val
            output = [0] * len(arr)
            
            # Store the frequency of each element
            for num in arr:
                count[num] += 1
                
            # Calculate cumulative sums (prefix sums)
            for i in range(1, len(count)):
                count[i] += count[i - 1]
                
            # Build the output array in reverse order to maintain stability
            for num in reversed(arr):
                output[count[num] - 1] = num
                count[num] -= 1
                
            return output



        costs = counting_sort(costs)
        count = 0
        for i in costs:
            if i <= coins:
                coins -= i
                count += 1
            else:
                break
        return count
        