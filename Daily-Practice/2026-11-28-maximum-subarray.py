# Maximum Subarray (Kadane's Algorithm)
# Date: 2026-11-28
# Problem: Given an integer array nums, find the subarray with the largest
# sum and return its sum. (LeetCode 53 - Medium)
# Approach: Kadane's algorithm - keep a running sum; whenever it drops
# below the current element, restart the subarray at that element.
# Time: O(n), Space: O(1).

def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([1]))                               # 1
    print(max_subarray([5, 4, -1, 7, 8]))                  # 23
