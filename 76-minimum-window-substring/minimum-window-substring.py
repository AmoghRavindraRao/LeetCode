from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        required = Counter(t)
        window = Counter()

        formed = 0
        needed = len(required)
        left = 0
        best_length = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in required and window[char] == required[char]:
                formed += 1

            while formed == needed:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in required
                    and window[left_char] < required[left_char]
                ):
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start : best_start + best_length]