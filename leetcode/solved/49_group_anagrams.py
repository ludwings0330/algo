from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ret = defaultdict(list)
        for str in strs:
            ret[''.join(sorted(list(str)))].append(str)
        return list(ret.values())

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagrams(strs))

