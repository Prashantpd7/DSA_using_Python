# Binary Search - Daily Practice
# Date: 2026-11-17
# Problem: Given a sorted array of integers, return the index of target
# if it exists, otherwise return -1. (LeetCode 704, Easy)
# Approach: classic binary search, O(log n) time, O(1) space.

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example
print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # 4
print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # -1
