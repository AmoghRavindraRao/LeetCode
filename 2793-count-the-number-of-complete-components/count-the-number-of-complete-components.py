from collections import defaultdict, deque

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        ans = 0

        for start in range(n):
            if start in seen:
                continue

            q = deque([start])
            seen.add(start)

            nodes = 0
            degree_sum = 0

            while q:
                node = q.popleft()
                nodes += 1
                degree_sum += len(graph[node])

                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)

            edges_in_component = degree_sum // 2

            if edges_in_component == nodes * (nodes - 1) // 2:
                ans += 1

        return ans
        