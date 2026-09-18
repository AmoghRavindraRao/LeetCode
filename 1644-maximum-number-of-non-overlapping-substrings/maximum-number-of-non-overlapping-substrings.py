class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            index = ord(ch) - ord("a")
            first[index] = min(first[index], i)
            last[index] = i

        def expand(left: int) -> int:
            """Return the smallest valid right boundary, or -1 if invalid."""
            right = last[ord(s[left]) - ord("a")]
            i = left

            while i <= right:
                index = ord(s[i]) - ord("a")

                if first[index] < left:
                    return -1

                right = max(right, last[index])
                i += 1

            return right

        intervals = []
        previous_end = -1

        for left, ch in enumerate(s):
            index = ord(ch) - ord("a")

            if first[index] != left:
                continue

            right = expand(left)

            if right == -1:
                continue

            if left > previous_end:
                intervals.append((left, right))
            else:
                intervals[-1] = (left, right)

            previous_end = right

        return [s[left:right + 1] for left, right in intervals]