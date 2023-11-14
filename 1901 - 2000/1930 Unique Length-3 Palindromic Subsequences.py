class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indexes = defaultdict(list)
        for i,c in enumerate(s): indexes[c].append(i)

        return sum(len(indexes[c1]) >= 2 and (i := bisect_right(indexes[c2],indexes[c1][0])) < len(indexes[c2]) and indexes[c2][i] < indexes[c1][-1] for c1 in ascii_lowercase for c2 in ascii_lowercase)
