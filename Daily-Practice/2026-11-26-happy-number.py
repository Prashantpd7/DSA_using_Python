# Daily Practice - 2026-11-26
# Problem: Happy Number (LeetCode 202, Easy)
# A number is happy if repeatedly replacing it by the sum of the squares
# of its digits eventually reaches 1. Detect loops with a seen set.

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


if __name__ == "__main__":
    print(is_happy(19))  # True
    print(is_happy(2))   # False
