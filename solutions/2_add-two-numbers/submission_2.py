from listnode import ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        linked_list = None
        answer_digits = []
        while l1 or l2:
            current_digit = 0
            if l1:
                current_digit += l1.val
                l1 = l1.next
            if l2:
                current_digit += l2.val
                l2 = l2.next
            current_digit += carry
            next_digit = current_digit % 10
            carry = current_digit // 10
            answer_digits = [next_digit] + answer_digits

        if carry:
            answer_digits = [carry] + answer_digits

        for i in answer_digits:
            linked_list = ListNode(i, linked_list)

        return linked_list

# Runtime: 65 ms, faster than 94.88% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 85.88% of Python3 online submissions for Add Two Numbers.
