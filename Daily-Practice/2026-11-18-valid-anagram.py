# Valid Anagram - 2026-11-18
# LeetCode 242 (Easy) - Hash map
# Check if two strings are anagrams of each other.

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True


print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
