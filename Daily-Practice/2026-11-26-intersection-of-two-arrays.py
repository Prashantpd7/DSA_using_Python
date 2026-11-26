# Daily Practice - 2026-11-26
# Problem: Intersection of Two Arrays (LeetCode 349, Easy)
# Given two integer arrays, return their intersection (unique elements only).

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))  # [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4] (order may vary)
