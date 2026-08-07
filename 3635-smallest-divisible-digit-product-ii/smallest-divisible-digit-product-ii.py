from functools import lru_cache


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Exponents of (2, 3, 5, 7) contributed by each digit.
        factors = (
            (0, 0, 0, 0),  # 0 is never used
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        )

        # Factorize t.
        required = []
        remaining_t = t

        for prime in (2, 3, 5, 7):
            exponent = 0
            while remaining_t % prime == 0:
                remaining_t //= prime
                exponent += 1
            required.append(exponent)

        # No nonzero decimal digit can supply any other prime factor.
        if remaining_t != 1:
            return "-1"

        req2, req3, req5, req7 = required

        @lru_cache(None)
        def min_digits_23(a: int, b: int) -> int:
            """
            Minimum digits needed to supply at least:
              a factors of 2 and b factors of 3.

            Digit 6 supplies both factors. The remaining factors are most
            efficiently supplied by 8 (three 2s) and 9 (two 3s).
            """
            best = a + b

            for sixes in range(min(a, b) + 1):
                twos = max(0, a - sixes)
                threes = max(0, b - sixes)

                count = (
                    sixes
                    + (twos + 2) // 3
                    + (threes + 1) // 2
                )
                best = min(best, count)

            return best

        def min_digits(a: int, b: int, c: int, d: int) -> int:
            # Only digits 5 and 7 contain their respective prime factors.
            return c + d + min_digits_23(a, b)

        def construct(length: int, need: tuple[int, int, int, int]) -> str:
            """Lexicographically smallest zero-free string of exact length."""
            a, b, c, d = need
            answer = []

            for position in range(length):
                positions_left = length - position - 1

                for digit in range(1, 10):
                    f2, f3, f5, f7 = factors[digit]

                    na = max(0, a - f2)
                    nb = max(0, b - f3)
                    nc = max(0, c - f5)
                    nd = max(0, d - f7)

                    if min_digits(na, nb, nc, nd) <= positions_left:
                        answer.append(str(digit))
                        a, b, c, d = na, nb, nc, nd
                        break

            return "".join(answer)

        n = len(num)

        # Count factors in the zero-free prefix and locate the first zero.
        prefix = [0, 0, 0, 0]
        first_zero = n

        for i, char in enumerate(num):
            digit = ord(char) - ord("0")

            if digit == 0:
                first_zero = i
                break

            contribution = factors[digit]
            for j in range(4):
                prefix[j] += contribution[j]

        # num itself is already valid.
        if first_zero == n and all(
            prefix[j] >= required[j] for j in range(4)
        ):
            return num

        if first_zero == n:
            # Start by changing the final digit. prefix must represent num[:i].
            start = n - 1
            last_factors = factors[ord(num[-1]) - ord("0")]
            for j in range(4):
                prefix[j] -= last_factors[j]
        else:
            # Any valid change must occur at or before the first zero.
            start = first_zero

        # Change the rightmost possible position. This minimizes the result.
        for i in range(start, -1, -1):
            current_digit = ord(num[i]) - ord("0")
            suffix_length = n - i - 1

            missing = (
                max(0, req2 - prefix[0]),
                max(0, req3 - prefix[1]),
                max(0, req5 - prefix[2]),
                max(0, req7 - prefix[3]),
            )

            for digit in range(current_digit + 1, 10):
                f2, f3, f5, f7 = factors[digit]

                suffix_need = (
                    max(0, missing[0] - f2),
                    max(0, missing[1] - f3),
                    max(0, missing[2] - f5),
                    max(0, missing[3] - f7),
                )

                if min_digits(*suffix_need) <= suffix_length:
                    suffix = construct(suffix_length, suffix_need)
                    return num[:i] + str(digit) + suffix

            if i > 0:
                removed = factors[ord(num[i - 1]) - ord("0")]
                for j in range(4):
                    prefix[j] -= removed[j]

        need = (req2, req3, req5, req7)
        answer_length = max(n + 1, min_digits(*need))
        return construct(answer_length, need)