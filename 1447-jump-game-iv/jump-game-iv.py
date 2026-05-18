class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n <= 1:
            return 0

        positions = {}
        for i in range(n):
            if arr[i] in positions:
                positions[arr[i]].append(i)
            else:
                positions[arr[i]] = [i]
        visited = set()
        q = [(0, 0)] 
        while q:
            pos, jumps = q.pop(0)
            
            if pos == n - 1:
                return jumps
            
            for next_pos in [pos-1, pos+1]:
                if 0 <= next_pos < n and next_pos not in visited:
                    visited.add(next_pos)
                    q.append((next_pos, jumps+1))
            
            if arr[pos] in positions:
                for next_pos in positions[arr[pos]]:
                    if next_pos not in visited:
                        visited.add(next_pos)
                        q.append((next_pos, jumps+1))
                
                del positions[arr[pos]]
        
        return -1 

        

        