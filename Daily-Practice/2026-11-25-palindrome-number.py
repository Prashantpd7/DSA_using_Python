# Palindrome Number - LeetCode 9 (Easy)
# Date: 2026-11-25
# Check whether an integer reads the same forwards and backwards.
# Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))   # True
    print(s.isPalindrome(-121))  # False
    print(s.isPalindrome(10))    # False
