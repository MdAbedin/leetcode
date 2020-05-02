class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return reduce(lambda a,b: a + (1 if b in jewels else 0), S, 0)
