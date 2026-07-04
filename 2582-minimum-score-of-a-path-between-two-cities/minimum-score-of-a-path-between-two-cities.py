from collections import defaultdict, deque

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        seen = set([1])
        q = deque([1])
        ans = float("inf")

        while q:
            city = q.popleft()

            for nei, dist in graph[city]:
                ans = min(ans, dist)

                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return ans