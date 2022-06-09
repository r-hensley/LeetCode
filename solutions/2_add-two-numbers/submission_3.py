from listnode import ListNode
from typing import Optional

from utils import convert_int_to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1  # a reference to c1. Editing c1 will reflect to l1
        c2 = l2
        carry = 0

        # Run until you approach the end of one of the lists
        while c1.next and c2:
            addition_result = c1.val + c2.val + carry
            c1.val = addition_result % 10
            carry = addition_result // 10

            c1 = c1.next
            c2 = c2.next

        # Now either c1 will be on its last element or c2 will be empty

        # If len(c1) > len(c2), so c2 is empty now and c1 still has some to go
        while c1.next:
            addition_result = c1.val + carry
            c1.val = addition_result % 10
            carry = addition_result // 10
            c1 = c1.next

        # Or, if len(c1) == len(c2), then c1.next was false, and c1/c2 are both on last element
        # Do just one addition for this case
        if c2:
            addition_result = c1.val + c2.val + carry
            c1.val = addition_result % 10
            carry = addition_result // 10

        # Now the only possible case is if c2 still has some way to go
        if c2 and c2.next:
            c1.next = c2.next  # push all the c2 stuff onto c1 and continue as normal
            while c1.next:
                c1 = c1.next
                addition_result = c1.val + carry
                c1.val = addition_result % 10
                carry = addition_result // 10

        # Now for sure we should be on the last legs of whatever kind of array setup we had
        # Take care of now just the last digit, there will be no more carrying
        # print(f"\nAfter main loops: \n{l1=}\n{c1=}, \n{c2=}, \n{addition_result=}, {carry=}")
        if not c2:
            addition_result = c1.val + carry
            c1.val = addition_result % 10
            carry = addition_result // 10

        # add the final carry
        if carry:
            # print(f"\nCarry: \n{l1=}\n{c1=}\n{c2=}\n{addition_result=}, {carry=}")
            final = ListNode(carry, None)
            c1.next = final

        return l1

if __name__ == "__main__":
    s = Solution()
    for i in [(342, 465), (0, 0), (9999999, 9999), (9999, 9999999), (199, 1)]:
        print("\n\n\n")
        l1 = convert_int_to_linked_list(i[0])
        l2 = convert_int_to_linked_list(i[1])
        res = s.addTwoNumbers(l1, l2)
        ans = convert_int_to_linked_list(i[0] + i[1])
        assert res == ans, f"\n{res}\n{ans}"


# Runtime: 71 ms, faster than 85.84% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 85.80% of Python3 online submissions for Add Two Numbers.