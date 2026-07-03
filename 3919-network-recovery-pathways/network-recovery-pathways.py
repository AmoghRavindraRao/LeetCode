from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n
        high = 0

        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))
                indeg[v] += 1
                high = max(high, cost)

        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def can(min_edge):
            INF = k + 1
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] > k:
                    continue

                for v, cost in graph[u]:
                    if cost >= min_edge:
                        nd = dist[u] + cost
                        if nd < dist[v] and nd <= k:
                            dist[v] = nd

            return dist[n - 1] <= k

        if not can(0):
            return -1

        ans = 0
        low = 0

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans