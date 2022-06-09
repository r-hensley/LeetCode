from listnode import ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def convert_int_to_linked_list(int_in: int) -> ListNode:
    int_str = str(int_in)
    last_node = ListNode(int(int_str[0]), None)
    for digit in int_str[1:]:
        last_node = ListNode(int(digit), last_node)

    return last_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ''
        carry = 0
        while l1 or l2:
            l1val = getattr(l1, 'val', 0)
            l2val = getattr(l2, 'val', 0)
            addition = l1val + l2val + carry
            next_digit = addition % 10
            carry = addition // 10
            result = str(next_digit) + result
            l1 = getattr(l1, 'next', None)
            l2 = getattr(l2, 'next', None)

        if carry:
            result = str(carry) + result

        linked_list = convert_int_to_linked_list(result)
        return linked_list


# Runtime: 146 ms, faster than 7.97% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 43.03% of Python3 online submissions for Add Two Numbers.