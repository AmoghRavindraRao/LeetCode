class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [(1, 0)]

        while stack:
            node, parent = stack.pop()
            up[0][node] = parent

            for nei in graph[node]:
                if nei != parent:
                    depth[nei] = depth[node] + 1
                    stack.append((nei, node))

        for j in range(1, LOG):
            for node in range(1, n + 1):
                up[j][node] = up[j - 1][up[j - 1][node]]

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff & (1 << j):
                    a = up[j][a]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]

            return up[0][a]

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[ancestor]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])

        return ans