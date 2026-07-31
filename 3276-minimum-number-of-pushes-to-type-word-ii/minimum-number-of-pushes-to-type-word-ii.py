from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        data = dict(counts.most_common())
        i,tot = 8, 0
        for apl, val in data.items():
            tot = tot + val * (i // 8)
            i += 1
        return tot