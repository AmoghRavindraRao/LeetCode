class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        if s[n - 1] == '1':
            return False
        reachable = [False] * n
        reachable[0] = True
        prefix = [0] * n
        prefix[0] = 1

        for j in range(1, n):
            if s[j] == '0':
                lo = max(0, j - maxJump)
                hi = j - minJump
                if hi >= 0:
                    window_sum = prefix[hi] - (prefix[lo - 1] if lo > 0 else 0)
                    reachable[j] = window_sum > 0

            prefix[j] = prefix[j - 1] + (1 if reachable[j] else 0)

        return reachable[n - 1]