from listnode import ListNode


def convert_int_to_linked_list(int_in: int) -> ListNode:
    int_str = str(int_in)
    last_node = ListNode(int(int_str[0]), None)
    for digit in int_str[1:]:
        last_node = ListNode(int(digit), last_node)

    print(int_in, '-->', last_node)
    return last_node


def convert_linked_list_to_int(linked_list: ListNode) -> int:
    result = ''
    while linked_list:
        result = str(linked_list.val) + result
        linked_list = linked_list.next

    return int(result)


def add_two_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    result = ''
    carry = 0
    # linked_list = None
    while l1 or l2:
        l1val = getattr(l1, 'val', 0)
        l2val = getattr(l2, 'val', 0)
        addition = l1val + l2val + carry
        next_digit = addition % 10
        carry = addition // 10
        result = str(next_digit) + result
        # linked_list = ListNode(next_digit, linked_list)
        print(l1val, l2val, addition, next_digit, carry, result)
        l1 = getattr(l1, 'next', None)
        l2 = getattr(l2, 'next', None)

    if carry:
        result = str(carry) + result

    # print(result)
    linked_list = convert_int_to_linked_list(result)
    print(linked_list)
    return linked_list


def test():
    l1 = convert_int_to_linked_list(123)
    l2 = convert_int_to_linked_list(456)
    l1p = convert_int_to_linked_list(123)
    print(l1==l1p)
    # 579
    x = add_two_linked_lists(l1, l2)
    y = convert_int_to_linked_list(123 + 456)
    print(convert_linked_list_to_int(x), convert_linked_list_to_int(y))
    assert x == y, f"{x}, {y}"
    # 33581
    assert add_two_linked_lists(convert_int_to_linked_list(8349), convert_int_to_linked_list(25232)) == convert_int_to_linked_list(8349 + 25232)


if __name__ == "__main__":
    test()
