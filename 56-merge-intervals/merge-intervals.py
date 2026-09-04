class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        if len(intervals) <= 1:
            return intervals
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                intervals.pop(i)
                continue
            else:
                i += 1
        
        return intervals