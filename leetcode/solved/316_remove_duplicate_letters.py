import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []

        for c in s:
            counter[c] -= 1

            if c in stack:
                continue

            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(c)

        return ''.join(stack)

print(Solution().removeDuplicateLetters("bcabc"))
