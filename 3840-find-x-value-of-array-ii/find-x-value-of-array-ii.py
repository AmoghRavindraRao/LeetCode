from typing import List

class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        identity = 1 % k
        product = [identity] * (2 * size)
        count = [[0] * k for _ in range(2 * size)]

        for i, value in enumerate(nums):
            remainder = value % k
            product[size + i] = remainder
            count[size + i][remainder] = 1

        def pull(node: int) -> None:
            left, right = 2 * node, 2 * node + 1
            left_product = product[left]
            product[node] = left_product * product[right] % k

            for r in range(k):
                count[node][r] = count[left][r]
            for r in range(k):
                count[node][left_product * r % k] += count[right][r]

        for node in range(size - 1, 0, -1):
            pull(node)

        answers = []

        for index, value, start, x in queries:
            node = size + index
            remainder = value % k
            product[node] = remainder
            count[node] = [0] * k
            count[node][remainder] = 1

            node //= 2
            while node:
                pull(node)
                node //= 2

            accumulated_product = identity
            accumulated_count = [0] * k
            left, right = size + start, 2 * size

            while left < right:
                if left & 1:
                    merged = accumulated_count[:]
                    for r in range(k):
                        merged[accumulated_product * r % k] += count[left][r]
                    accumulated_count = merged
                    accumulated_product = accumulated_product * product[left] % k
                    left += 1

                left //= 2
                right //= 2

            answers.append(accumulated_count[x])

        return answers
        