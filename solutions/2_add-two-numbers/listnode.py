from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<ListNode: value={self.val}, next={self.next}>"

    def __eq__(self, other: ListNode):
        now = self
        while now:
            try:
                if now.val != other.val:
                    return
                if now.next != other.next:
                    return
            except AttributeError:
                return
            now = now.next
            other = other.next
        return True


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(3, ListNode(4, None)))
    c1 = l1
    c1.val = 5
    c1 = c1.next
    print(l1, c1)

    c1.val = 6
    c1 = c1.next
    print(l1, c1)