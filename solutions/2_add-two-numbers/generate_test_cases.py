import random
from typing import Optional

import utils
from listnode import ListNode


class TestCase:
    def __init__(self, _l1, _l2, _n1, _n2, answer):
        self.l1: ListNode = _l1
        self.l2: ListNode = _l2
        self.n1: int = _n1
        self.n2: int = _n2
        self.answer: int = answer


def generate_test_cases(num_of_cases: int) -> list[TestCase]:
    test_cases = []
    n1 = n2 = 0
    l1 = l2 = None
    for case_num in range(num_of_cases):
        case_length = random.randint(1, 100)
        n1 = random.randint(10 ** (case_length - 1), 10 ** case_length - 1)  # generate random case_length-digit number
        l1 = utils.convert_int_to_linked_list(n1)

        case_length = random.randint(1, 100)
        n2 = random.randint(10 ** (case_length - 1), 10 ** case_length - 1)  # generate random case_length-digit number
        l2 = utils.convert_int_to_linked_list(n2)

        test_case = TestCase(l1, l2, n1, n2, n1 + n2)
        test_cases.append(test_case)

    return test_cases


if __name__ == "__main__":
    test_cases = generate_test_cases(20)

    for test in test_cases:
        assert utils.add_two_linked_lists(test.l1, test.l2) == utils.convert_int_to_linked_list(test.answer), \
            f"{test.n1}, {test.n2}, {test.answer}, {utils.convert_int_to_linked_list(test.answer)}"
        print(f"{test.n1} + {test.n2} = {test.answer}")

