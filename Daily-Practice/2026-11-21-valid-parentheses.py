# Valid Parentheses - Daily Practice
# Date: 2026-11-21
# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. An input string is valid if open brackets
# are closed by the same type of brackets and in the correct order.
# Difficulty: Easy | Topic: Stack

def is_valid(s: str) -> bool:
    """Return True if every bracket in s is closed correctly, else False."""
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    for s, expected in tests:
        result = is_valid(s)
        print(f"{s!r}: {result} (expected {expected})")
        assert result == expected
    print("All tests passed.")
