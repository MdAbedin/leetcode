class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return sum(c1*c2 for c1,c2 in pairwise([row.count("1") for row in bank if "1" in row]))
