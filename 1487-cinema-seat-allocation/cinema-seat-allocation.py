class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        data = {}
        for i, j in reservedSeats:
            if j != 10 and j != 1:
                if i in data:
                    data[i].append(j)
                else:
                    data[i] = [j]

        count = (n - len(data)) * 2

        for row in data:
            reserved = set(data[row])

            left_free = all(seat not in reserved for seat in range(2, 6))
            middle_free = all(seat not in reserved for seat in range(4, 8))
            right_free = all(seat not in reserved for seat in range(6, 10))

            if left_free and right_free:
                count += 2
            elif left_free or middle_free or right_free:
                count += 1
        
        return count
        