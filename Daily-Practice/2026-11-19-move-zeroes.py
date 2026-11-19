# Move Zeroes - LeetCode 283 (Easy)
# Date: 2026-11-19
# Move all zeroes to the end, keeping the relative order of non-zero elements.
# Two pointers, in place, O(n) time, O(1) space.

def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
    print(move_zeroes([0]))               # [0]
