class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = 1 << max(nums).bit_length()
        count = [0] * size

        for x in set(nums):
            count[x] = 1

        def fwht(a):
            step = 1
            while step < size:
                for i in range(0, size, step * 2):
                    for j in range(i, i + step):
                        x, y = a[j], a[j + step]
                        a[j], a[j + step] = x + y, x - y
                step *= 2

        fwht(count)

        # Three-way XOR convolution.
        count = [x ** 3 for x in count]

        fwht(count)

        # The inverse FWHT divides every value by size.
        return sum(x // size > 0 for x in count)      