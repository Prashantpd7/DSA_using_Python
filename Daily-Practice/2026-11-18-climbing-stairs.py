# Climbing Stairs - 2026-11-18
# LeetCode 70 (Easy) - Dynamic programming
# Count distinct ways to climb n steps, taking 1 or 2 steps at a time.

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
print(climb_stairs(5))  # 8
