# Daily Practice - 2026-11-20
# Problem: Linked List Cycle (LeetCode 141, Easy)
# Return True if the linked list has a cycle.

from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's tortoise and hare: O(n) time, O(1) space.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    # 3 -> 2 -> 0 -> -4, tail links back to node 2 (cycle).
    a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    a.next, b.next, c.next, d.next = b, c, d, b
    print(Solution().hasCycle(a))  # True
    e, f = ListNode(1), ListNode(2)
    e.next = f
    print(Solution().hasCycle(e))  # False
