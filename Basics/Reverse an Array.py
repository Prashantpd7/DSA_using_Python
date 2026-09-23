# Question: Reverse an Array
# Given an array of integers, reverse the array in-place.
# Example:
#   Input:  [1, 2, 3, 4, 5]
#   Output: [5, 4, 3, 2, 1]
# Approach: Two-pointer technique - swap elements from both ends
# moving towards the center.
# Time Complexity: O(n), Space Complexity: O(1)

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))
