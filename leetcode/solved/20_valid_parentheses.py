class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c not in table:
                stack.append(c)
            elif not stack or table[c] != stack.pop():
                return False

        return len(stack) == 0


print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("()[][][[]]"))