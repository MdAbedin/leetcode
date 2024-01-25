class Solution:
    @cache
    def longestCommonSubsequence(self, text1: str, text2: str, i1 = 0, i2 = 0) -> int:
        if i1 == len(text1) or i2 == len(text2): return 0
        return 1+self.longestCommonSubsequence(text1,text2,i1+1,i2+1) if text1[i1] == text2[i2] else max(self.longestCommonSubsequence(text1,text2,i1+1,i2),self.longestCommonSubsequence(text1,text2,i1,i2+1))
