import time
import random
import sys


class Solution:
    """Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the
    same element twice.

    You can return the answer in any order."""
    def __init__(self):
        # Test case list is ([nums], target, [output])
        # test_cases = [([2, 7, 11, 15], 9, [0, 1]),
        #               ([3, 2, 4], 6, [1, 2]),
        #               ([3, 3], 6, [0, 0]),
        #               ([5, 2, 7, 1, 5, 3, 16], 5, [1, 5])]

        if test := True:
            self.test_cases: list[tuple[list, int, list]] = self.generate_test_cases(0)
            self.test_cases.append((list(range(1, 10001)), 19999, [9998, 9999]))
            print("First test case: ", self.test_cases[0])
            # self.test_solutions(self.solution_one)
            # self.test_solutions(self.solution_two)
            # self.test_solutions(self.solution_three)
            self.test_solutions(self.solution_four)

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Performs best solution (four)"""
        return self.solution_four(nums, target)

    def test_solutions(self, solution_function):
        """Tests given case"""
        start = time.perf_counter()
        for case in self.test_cases:
            assert sorted(solution_function(case[0], case[1])) == sorted(case[2])
        finish = time.perf_counter()
        print(f"{solution_function.__name__} finished in {finish - start} seconds")

    @staticmethod
    def generate_test_cases(num_of_cases: int) -> list[tuple[list, int, list]]:
        """Generates num_of_cases number of test cases to test the code"""
        test_cases = []

        # generate num_of_cases number of test cases
        while len(test_cases) < num_of_cases:

            # each test case should be a list of random length 2 to 200
            while True:
                test_case = [random.randint(int(-1e9), int(1e9)) for _ in range(10000)]

                # make sure there's no duplicates of the first two numbers elsewhere in the list
                if test_case.count(test_case[0]) == 1 and test_case.count(test_case[1]) == 1:
                    break

            target_candidate = test_case[0] + test_case[1]

            # check to make sure there's not duplicate ways to get the target in this set
            def check_test_case_validity():
                for i_idx, i in enumerate(test_case):
                    for j_idx, j in enumerate(test_case):
                        if i_idx >= j_idx:
                            continue  # to avoid double counting
                        if i_idx == 0 and j_idx == 1:
                            continue  # the test case

                        # check if there's another way to get the target candidate other than the first two nums
                        if i + j == target_candidate:
                            return False  # not a valid test case

                # for loops above never returned
                return True  # a valid test case

            if check_test_case_validity():
                num_one = test_case[0]
                num_two = test_case[1]
                random.shuffle(test_case)
                test_cases.append(
                    (test_case,
                     target_candidate,
                     [test_case.index(num_one), test_case.index(num_two)]
                     )
                )

        return test_cases

    @staticmethod
    def solution_one(nums: list[int], target: int) -> list[int]:
        """Simplest algorithm that fully loops over the list twice"""
        candidate_solution = None
        for i_idx, i in enumerate(nums):
            for j_idx, j in enumerate(nums):
                if i_idx != j_idx and i + j == target:
                    candidate_solution = [i_idx, j_idx]

        if candidate_solution:
            return candidate_solution
        else:
            raise ValueError("No valid solution found")

    @staticmethod
    def solution_two(nums: list[int], target: int) -> list[int]:
        """Similar to solution one but this one ejects out of the list as soon as it finds the solution.
        It assumes there's no duplicate solutions in the list."""
        for i_idx, i in enumerate(nums):
            for j_idx, j in enumerate(nums):
                if i_idx != j_idx and i + j == target:
                    return [i_idx, j_idx]

    @staticmethod
    def solution_three(nums: list[int], target: int) -> list[int]:
        """Now this solution sorts the list first numerically, and once two numbers add up to something higher than
        the target, we know we've gone too far so we can stop

        Turns out the sorting process ends up making this solution take longer than the others"""
        sorted_nums = sorted(nums)
        for i in sorted_nums:
            for j in sorted_nums:
                if i + j > target:
                    break
                elif i + j == target:
                    i_idx = nums.index(i)
                    j_idx = nums.index(j)
                    return [i_idx, j_idx]

    @staticmethod
    def solution_four(nums: list[int], target: int) -> list[int]:
        """Solution two, but looks up index of (target - i) for j"""
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


# Runtime: 234 ms, faster than 36.08% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 49.06% of Python3 online submissions for Two Sum.
