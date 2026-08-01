class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def best(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            take_left = nums[left] - best(left + 1, right)
            take_right = nums[right] - best(left, right - 1)

            return max(take_left, take_right)

        return best(0, len(nums) - 1) >= 0