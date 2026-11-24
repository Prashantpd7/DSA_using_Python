# Daily Practice - 2026-11-24
# Problem: Reverse Linked List (LeetCode 206, Easy)
# Reverse a singly linked list and return the reversed list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def to_list(head: Optional[ListNode]) -> list:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(to_list(reverse_list(head)))  # [5, 4, 3, 2, 1]
    print(to_list(reverse_list(None)))  # []
