from typing import List
from itertools import combinations
from math import lcm
from bisect import bisect_left

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        coins = [
            coin for i, coin in enumerate(coins)
            if all(coin % smaller != 0 for smaller in coins[:i])
        ]

        terms = [
            (lcm(*group), 1 if size % 2 else -1)
            for size in range(1, len(coins) + 1)
            for group in combinations(coins, size)
        ]

        def count(x):
            return sum(sign * (x // multiple) for multiple, sign in terms)

        upper = coins[0] * k
        return bisect_left(range(1, upper + 1), k, key=count) + 1