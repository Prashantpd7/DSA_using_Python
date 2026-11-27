# Remove Duplicates from Sorted Array
# Date: 2026-11-27 | LeetCode 26 (Easy) | Two pointers
# Remove duplicates in-place and return the new length.

def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k, nums[:k])  # 5 [0, 1, 2, 3, 4]
