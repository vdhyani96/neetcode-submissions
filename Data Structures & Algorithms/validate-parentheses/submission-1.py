class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if (item == ')' and stack and stack[-1] == '(') or \
                (item == '}' and stack and stack[-1] == '{') or \
                (item == ']' and stack and stack[-1] == '['):
                stack.pop()
                continue
            stack.append(item)
        return True if len(stack) == 0 else False