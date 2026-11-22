# Merge Two Sorted Lists - LeetCode 21 (Easy)
# Date: 2026-11-22
# Merge two sorted linked lists into one sorted list.

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

def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

def from_list(vals):
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

if __name__ == "__main__":
    print(to_list(merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
