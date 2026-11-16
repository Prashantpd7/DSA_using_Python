# Daily Practice - 2026-11-16
# Problem: Maximum Subarray (LeetCode 53, Medium)
# Given an integer array nums, find the contiguous subarray with the
# largest sum and return its sum. (Kadane's algorithm, O(n) time.)

def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of any contiguous subarray."""
    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([5, 4, -1, 7, 8]))                # 23
