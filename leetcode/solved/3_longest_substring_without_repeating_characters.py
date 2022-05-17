from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque()
        answer = -1

        for c in s:
            if dq and c in dq:
                answer = max(answer, len(dq))

                while dq and dq.popleft() != c:
                    pass
            dq.append(c)

        return max(answer, len(dq))

print(Solution().lengthOfLongestSubstring("abcabcbb"))