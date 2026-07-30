class Solution:
    def minimumPushes(self, word: str) -> int:
        i = 1
        n = len(word)
        push = 0
        while i <= n // 8:
            push = push + (i) * 8
            i += 1
        return push + (i * (n % 8))