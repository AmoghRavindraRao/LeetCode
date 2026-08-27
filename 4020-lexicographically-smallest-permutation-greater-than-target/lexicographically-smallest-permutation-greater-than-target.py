from typing import List

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        prefix = []
        i = 0
        n = len(s)

        while i < n:
            index = ord(target[i]) - ord('a')

            if count[index] == 0:
                break

            prefix.append(target[i])
            count[index] -= 1
            i += 1

        while True:
            # Try to make this position slightly greater.
            if i < n:
                current = ord(target[i]) - ord('a')

                for bigger in range(current + 1, 26):
                    if count[bigger] > 0:
                        count[bigger] -= 1

                        suffix = ''.join(
                            chr(letter + ord('a')) * count[letter]
                            for letter in range(26)
                        )

                        return (
                            ''.join(prefix)
                            + chr(bigger + ord('a'))
                            + suffix
                        )

            if i == 0:
                return ""

            i -= 1
            restored = ord(prefix.pop()) - ord('a')
            count[restored] += 1