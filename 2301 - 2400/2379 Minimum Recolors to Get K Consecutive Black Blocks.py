class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        return min(k-chars.count("B") for chars in zip(*[blocks[i:] for i in range(k)]))
