import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1 <= s.length <= 2*100,000
        s = re.sub('[^a-z0-9]', '', s.lower())
        return s == s[::-1]



inputs = ["A man, a plan, a canal: Panama", "race a car", " "]

for s in inputs:
    print(Solution.isPalindrome(Solution(), s))
