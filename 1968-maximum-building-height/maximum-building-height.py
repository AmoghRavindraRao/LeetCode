class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])

        # If building n has no explicit restriction, its natural max is n - 1
        has_n = False
        for idx, _ in restrictions:
            if idx == n:
                has_n = True
                break

        if not has_n:
            restrictions.append([n, n - 1])

        restrictions.sort()

        # Left to right: each restricted height cannot exceed previous + distance
        for i in range(1, len(restrictions)):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)

        # Right to left: each restricted height cannot exceed next + distance
        for i in range(len(restrictions) - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)

        ans = 0

        # Max peak between two restricted buildings
        for i in range(1, len(restrictions)):
            left_id, left_h = restrictions[i - 1]
            right_id, right_h = restrictions[i]

            dist = right_id - left_id
            peak = (left_h + right_h + dist) // 2
            ans = max(ans, peak)

        return ans