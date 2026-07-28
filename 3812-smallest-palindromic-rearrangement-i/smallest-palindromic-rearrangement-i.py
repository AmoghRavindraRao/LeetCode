class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        data = dict(sorted(counts.items()))
        print(data)
        start, mid = '', ''
        for alp, val in data.items():
            if val % 2 != 0:
                mid += alp
            temp = val // 2
            start = start + (alp * temp)
        return start + mid + start[::-1]