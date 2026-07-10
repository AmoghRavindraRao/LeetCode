class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nodes = sorted((nums[i], i) for i in range(n))

        vals = [x for x, _ in nodes]
        pos = [0] * n

        for i, (_, original_index) in enumerate(nodes):
            pos[original_index] = i

        # farthest[i] = farthest sorted position reachable from i in one edge
        farthest = [0] * n
        r = 0

        for l in range(n):
            while r + 1 < n and vals[r + 1] - vals[l] <= maxDiff:
                r += 1
            farthest[l] = r

        LOG = 17
        while (1 << LOG) <= n:
            LOG += 1

        jump = [farthest]

        for _ in range(1, LOG):
            prev = jump[-1]
            jump.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            left = pos[u]
            right = pos[v]

            if left > right:
                left, right = right, left

            if farthest[left] >= right:
                ans.append(1)
                continue

            cur = left
            steps = 0

            for p in range(LOG - 1, -1, -1):
                nxt = jump[p][cur]
                if nxt < right:
                    cur = nxt
                    steps += 1 << p

            if cur == jump[0][cur]:
                ans.append(-1)
            else:
                ans.append(steps + 1)

        return ans