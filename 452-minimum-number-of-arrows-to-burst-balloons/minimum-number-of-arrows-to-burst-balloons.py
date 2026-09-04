class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        i = 1
        end = points[0][1]
        for balloon in points[i:]:
            if balloon[0] > end:
                i += 1
                end = balloon[1]
            else:
                end = min(end, balloon[1])
        
        return i