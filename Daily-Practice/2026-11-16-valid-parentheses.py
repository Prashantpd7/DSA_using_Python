# Daily Practice - 2026-11-16
# Problem: Valid Parentheses (LeetCode 20, Easy)
# Given a string s containing just the characters '()[]{}',
# determine if the input string is valid.

def is_valid(s: str) -> bool:
    """Return True if every opening bracket is closed in the correct order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack


if __name__ == "__main__":
    print(is_valid("()[]{}"))  # True
    print(is_valid("(]"))      # False
    print(is_valid("{[]}"))    # True
