# Group Anagrams - LeetCode 49 (Medium)
# Date: 2026-11-19
# Group words that are anagrams of each other using the sorted word as key.
# O(n * k log k) time, O(n * k) space.

from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
