class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        def count_up_to(limit):
            if limit <= 0:
                return 0

            digits = [int(c) for c in str(limit)]
            n = len(digits)
            memo = {}

            def dfs(pos, tight, started, prev2, prev1):
                if pos == n:
                    return 1, 0

                key = (pos, started, prev2, prev1)
                if not tight and key in memo:
                    return memo[key]

                max_digit = digits[pos] if tight else 9
                ways = 0
                total = 0

                for d in range(max_digit + 1):
                    next_tight = tight and d == digits[pos]

                    if not started and d == 0:
                        child_ways, child_total = dfs(
                            pos + 1,
                            next_tight,
                            False,
                            -1,
                            -1
                        )
                        ways += child_ways
                        total += child_total
                    else:
                        add = 0

                        if not started:
                            next_prev2 = -1
                            next_prev1 = d
                        elif prev2 == -1:
                            next_prev2 = prev1
                            next_prev1 = d
                        else:
                            if prev2 < prev1 > d or prev2 > prev1 < d:
                                add = 1

                            next_prev2 = prev1
                            next_prev1 = d

                        child_ways, child_total = dfs(
                            pos + 1,
                            next_tight,
                            True,
                            next_prev2,
                            next_prev1
                        )

                        ways += child_ways
                        total += child_total + add * child_ways

                if not tight:
                    memo[key] = (ways, total)

                return ways, total

            return dfs(0, True, False, -1, -1)[1]

        return count_up_to(num2) - count_up_to(num1 - 1)