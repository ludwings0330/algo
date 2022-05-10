import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = re.sub('[^a-z]',' ', paragraph.lower())
        paragraph = [content for content in paragraph.split(' ') if content not in banned and content]
        counter = collections.Counter(paragraph)

        ret = counter.most_common(1)
        return ret[0][0]
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(Solution.mostCommonWord(Solution(), paragraph, banned))
