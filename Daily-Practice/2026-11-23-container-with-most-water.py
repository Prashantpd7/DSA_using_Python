# Daily Practice - 2026-11-23
# Problem: Container With Most Water (Two Pointers, Medium)
# Given an array of heights, find two lines that together with the
# x-axis form a container holding the most water.

from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        if height[left] < height[right]:
            best = max(best, width * height[left])
            left += 1
        else:
            best = max(best, width * height[right])
            right -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))  # 1
