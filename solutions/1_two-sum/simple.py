class Solution:
    """Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the
    same element twice.

    You can return the answer in any order."""
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        """Similar to solution one but this one ejects out of the list as soon as it finds the solution.
        It assumes there's no duplicate solutions in the list."""
        max_value = max(nums)
        for i_idx, i in enumerate(nums):
            if i + max_value < target:
                continue
            try:
                j_idx = nums.index(target - i)
            except ValueError:
                continue
            if i_idx != j_idx:
                return [i_idx, j_idx]

# Runtime: 61 ms (beats 93.41%)
# Memory Usage: 14.9 MB (beats 94.96%)
# https://leetcode.com/submissions/detail/717153259/