# Merge Two Sorted Lists - Daily Practice
# Date: 2026-11-17
# Problem: Merge two sorted linked lists into one sorted list and
# return its head. (LeetCode 21, Easy)
# Approach: dummy node + two pointers, O(n + m) time, O(1) space.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


# Example
print(to_list(merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
