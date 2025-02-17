class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(set(chain(*map(accumulate,permutations(tiles)))))
