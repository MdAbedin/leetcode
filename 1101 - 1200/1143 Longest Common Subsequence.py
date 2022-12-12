class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs_row = [0]*len(text1)
        
        for i in range(len(text2)):
            lcs_row_temp = [0]*len(text1)
            
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    lcs_row_temp[j] = (lcs_row[j-1] if j-1 >= 0 else 0) + 1
                else:
                    lcs_row_temp[j] = max(lcs_row_temp[j-1] if j-1 >= 0 else 0, lcs_row[j])
                
            lcs_row = lcs_row_temp
            
        return lcs_row[-1]
