from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_num = max(nums)

        # Frequency of each value.
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        # exact[g] will store the number of pairs whose GCD is exactly g.
        exact = [0] * (max_num + 1)

        # Process from large to small so counts for larger multiples are known.
        for g in range(max_num, 0, -1):
            divisible_count = 0

            for multiple in range(g, max_num + 1, g):
                divisible_count += freq[multiple]

            # Every pair here has a GCD divisible by g.
            pair_count = divisible_count * (divisible_count - 1) // 2

            # Remove pairs whose GCD is a larger multiple of g.
            for multiple in range(g + g, max_num + 1, g):
                pair_count -= exact[multiple]

            exact[g] = pair_count

        # prefix[g] = number of pairs with GCD <= g.
        prefix = [0] * (max_num + 1)
        for g in range(1, max_num + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        # A zero-based query q belongs to the first prefix count > q.
        return [bisect_right(prefix, query) for query in queries]