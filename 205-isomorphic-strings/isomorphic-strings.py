class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}
        used = set()

        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in used:
                    return False

                mapping[s[i]] = t[i]
                used.add(t[i])

            elif mapping[s[i]] != t[i]:
                return False

        return True