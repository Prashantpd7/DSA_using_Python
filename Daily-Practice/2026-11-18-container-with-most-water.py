# Container With Most Water - 2026-11-18
# LeetCode 11 (Medium) - Two pointers
# Find two lines that together with the x-axis form a container
# holding the most water.

def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 1]))                        # 1
