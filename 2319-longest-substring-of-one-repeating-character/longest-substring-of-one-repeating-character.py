from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        chars = list(s)
        n = len(chars)
        tree = [None] * (4 * n)

        def merge(left_node, right_node):
            (
                left_len,
                left_char,
                left_right_char,
                left_prefix,
                left_suffix,
                left_best,
            ) = left_node

            (
                right_len,
                right_left_char,
                right_char,
                right_prefix,
                right_suffix,
                right_best,
            ) = right_node

            total_len = left_len + right_len
            prefix = left_prefix
            suffix = right_suffix
            best = max(left_best, right_best)

            if left_right_char == right_left_char:
                best = max(best, left_suffix + right_prefix)

                if left_prefix == left_len:
                    prefix = left_len + right_prefix
                if right_suffix == right_len:
                    suffix = right_len + left_suffix

            return (
                total_len,
                left_char,
                right_char,
                prefix,
                suffix,
                best,
            )

        def build(node, start, end):
            if start == end:
                character = chars[start]
                tree[node] = (1, character, character, 1, 1, 1)
                return

            middle = (start + end) // 2

            build(node * 2, start, middle)
            build(node * 2 + 1, middle + 1, end)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, index, character):
            if start == end:
                tree[node] = (1, character, character, 1, 1, 1)
                return

            middle = (start + end) // 2

            if index <= middle:
                update(node * 2, start, middle, index, character)
            else:
                update(node * 2 + 1, middle + 1, end, index, character)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        answer = []

        for index, character in zip(queryIndices, queryCharacters):
            chars[index] = character
            update(1, 0, n - 1, index, character)

            answer.append(tree[1][5])

        return answer