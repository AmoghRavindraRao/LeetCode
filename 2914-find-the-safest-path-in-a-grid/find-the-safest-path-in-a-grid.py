from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 1. Multi-source BFS from all thieves.
        # dist[r][c] = distance from cell (r, c) to nearest thief.
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # 2. Max-heap path search.
        # We want the path that maximizes the minimum dist value along the path.
        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]

        heap = [(-dist[0][0], 0, 0)]

        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe

            if r == n - 1 and c == n - 1:
                return safe

            if safe < best[r][c]:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    next_safe = min(safe, dist[nr][nc])

                    if next_safe > best[nr][nc]:
                        best[nr][nc] = next_safe
                        heapq.heappush(heap, (-next_safe, nr, nc))

        return 0