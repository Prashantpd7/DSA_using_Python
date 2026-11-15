# Reverse String - Daily Practice 15 Nov 2026
# Reverse a string in place using two pointers. O(n) time, O(1) extra space.

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == "__main__":
    print(reverse_string(["h", "e", "l", "l", "o"]))  # ['o', 'l', 'l', 'e', 'h']
