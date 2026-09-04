class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))

            if temp not in map:
                map[temp] = []
            map[temp].append(strs[i])
        ans = []
        for key, val in map.items():
            ans.append(val)
        
        return ans