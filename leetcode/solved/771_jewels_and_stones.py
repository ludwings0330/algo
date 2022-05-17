class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([c for c in stones if c in jewels])