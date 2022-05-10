class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1 <= s.length <= 1000
        ret = s[0]
        for i in range(len(s) - 1):
            left, right = i, i+1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                ret = s[left:right + 1] if len(ret) < right - left + 1 else ret
                left -= 1
                right += 1

            mid = i
            left, right = mid - 1, mid + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                ret = s[left:right + 1] if len(ret) < right - left + 1else ret
                left -= 1
                right += 1
        return ret


ss = ["babad", "babab", "cbbd", "aaaaaaaaaaaaaaaaaaaaaabbbb"]
sol = Solution()
for s in ss:
    print(sol.longestPalindrome(s))
