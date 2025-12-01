def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != pairs.get(ch):
                return False
            stack.pop()

    return len(stack) == 0

print(isValid("{{{"))