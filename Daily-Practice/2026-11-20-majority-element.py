# Daily Practice - 2026-11-20
# Problem: Majority Element (LeetCode 169, Easy)
# Find the element that appears more than n // 2 times.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting: O(n) time, O(1) space.
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))  # 3
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
