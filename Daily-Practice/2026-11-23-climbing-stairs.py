# Daily Practice - 2026-11-23
# Problem: Climbing Stairs (Dynamic Programming, Easy)
# You are climbing a staircase of n steps. Each time you can climb
# 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    print(climb_stairs(2))  # 2
    print(climb_stairs(3))  # 3
    print(climb_stairs(5))  # 8
