# First Unique Character in a String
# Date: 2026-11-27 | LeetCode 387 (Easy) | Hash map
# Find the index of the first non-repeating character, or -1.

from collections import Counter

def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

print(first_uniq_char("leetcode"))       # 0
print(first_uniq_char("loveleetcode"))   # 2
print(first_uniq_char("aabb"))           # -1
