from bisect import bisect_right
class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        arr = sorted(coins)

        starts = []
        prefix = []
        candidates = set()

        running_total = 0

        for l, r, money in arr:
            starts.append(l)

            segment_total = (r - l + 1) * money
            running_total += segment_total
            prefix.append(running_total)

            candidates.add(l)

            start = r - k + 1
            if start >= 1:
                candidates.add(start)

        def money_up_to(x):
            if x < 1:
                return 0
            i = bisect_right(starts, x) - 1

            if i < 0:
                return 0

            l, r, money = arr[i]
            money_before = prefix[i - 1] if i > 0 else 0

            if x <= r:
                covered_length = x - l + 1
                return money_before + covered_length * money
            return prefix[i]

        answer = 0

        for start in candidates:
            end = start + k - 1

            window_money = money_up_to(end) - money_up_to(start - 1)
            answer = max(answer, window_money)

        return answer


