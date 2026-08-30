class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Remove both from front
        front = right + 1

        # Remove both from back
        back = n - left

        # Remove one from front and one from back
        both_sides = (left + 1) + (n - right)

        return min(front, back, both_sides)
