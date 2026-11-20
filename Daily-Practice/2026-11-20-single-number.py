# Daily Practice - 2026-11-20
# Problem: Single Number (LeetCode 136, Easy)
# Every element appears twice except one; find the one that appears once.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR cancels duplicates (a ^ a == 0, a ^ 0 == a): O(n) time, O(1) space.
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))  # 1
    print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
