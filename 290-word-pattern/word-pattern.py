class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        used = set()
        arr = s.split()
        m = len(arr)
        n = len(pattern)
        if n < m or n > m:
            return False
        
        for i in range(n):
            if pattern[i] not in map:
                if arr[i] in used:
                    return False
                map[pattern[i]] = arr[i]
                used.add(arr[i])

            elif map[pattern[i]] != arr[i]:
                return False
        
        return True