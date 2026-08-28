class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        odd = [i for i in range(26) if count[i] % 2]

        if len(odd) != n % 2:
            return ""

        middle = chr(odd[0] + ord('a')) if odd else ""
        half_count = [frequency // 2 for frequency in count]
        half_length = n // 2
        bound = target[:half_length]

        def make_palindrome(left):
            return left + middle + left[::-1]

        bound_count = [0] * 26
        for char in bound:
            bound_count[ord(char) - ord('a')] += 1

        if bound_count == half_count:
            palindrome = make_palindrome(bound)

            if palindrome > target:
                return palindrome

        remaining = half_count[:]
        prefix = []
        i = 0

        while i < half_length:
            index = ord(bound[i]) - ord('a')

            if remaining[index] == 0:
                break

            remaining[index] -= 1
            prefix.append(bound[i])
            i += 1

        while True:
            if i < half_length:
                current = ord(bound[i]) - ord('a')

                for larger in range(current + 1, 26):
                    if remaining[larger]:
                        remaining[larger] -= 1

                        suffix = ''.join(
                            chr(char + ord('a')) * remaining[char]
                            for char in range(26)
                        )

                        left = (
                            ''.join(prefix)
                            + chr(larger + ord('a'))
                            + suffix
                        )

                        return make_palindrome(left)

            if i == 0:
                return ""

            i -= 1
            restored = ord(prefix.pop()) - ord('a')
            remaining[restored] += 1