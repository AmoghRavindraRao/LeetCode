from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        litter_index = {}

        for row in range(rows):
            for col in range(cols):
                if classroom[row][col] == "S":
                    start_row, start_col = row, col
                elif classroom[row][col] == "L":
                    litter_index[(row, col)] = len(litter_index)

        full_mask = (1 << len(litter_index)) - 1

        if full_mask == 0:
            return 0

        best_energy = [
            [[-1] * (full_mask + 1) for _ in range(cols)]
            for _ in range(rows)
        ]

        queue = deque([
            (start_row, start_col, 0, energy, 0)
        ])

        best_energy[start_row][start_col][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col, mask, remaining, moves = queue.popleft()

            if remaining == 0:
                continue

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                cell = classroom[new_row][new_col]

                if cell == "X":
                    continue

                new_energy = remaining - 1
                new_mask = mask

                if cell == "R":
                    new_energy = energy

                elif cell == "L":
                    litter = litter_index[(new_row, new_col)]
                    new_mask |= 1 << litter

                if new_mask == full_mask:
                    return moves + 1

                if new_energy <= best_energy[new_row][new_col][new_mask]:
                    continue

                best_energy[new_row][new_col][new_mask] = new_energy
                queue.append((
                    new_row,
                    new_col,
                    new_mask,
                    new_energy,
                    moves + 1
                ))

        return -1