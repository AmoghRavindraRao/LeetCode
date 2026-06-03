class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        mn = float('inf')
        sm = float('inf')
        for i in range(len(landStartTime)):
            sm = min(sm, landStartTime[i] + landDuration[i])
        
        for i in range(len(waterStartTime)):
            if waterStartTime[i] >= sm:
                mn = min(mn, waterStartTime[i] + waterDuration[i])
            else:
                mn = min(mn, sm + waterDuration[i])
        
        sm = float('inf')
        for i in range(len(waterStartTime)):
            sm = min(sm, waterStartTime[i] + waterDuration[i])
        
        for i in range(len(landStartTime)):
            if landStartTime[i] >= sm:
                mn = min(mn, landStartTime[i] + landDuration[i])
            else:
                mn = min(mn, sm + landDuration[i])
        
        return (mn)        