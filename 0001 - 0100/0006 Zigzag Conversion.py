class Solution:
    """
    N = length of s
    Time:  O(N)
    Space: O(N)
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        
        ans = []
        cycle_len = (numRows-1)*2
        
        for r in range(numRows):
            if r in (0, numRows-1):
                ans.append(s[r : len(s) : cycle_len])
            else:
                i = r
                skip = cycle_len - 2*r
                
                while i < len(s):
                    ans.append(s[i])
                    i += skip
                    skip = cycle_len - skip
        
        return "".join(ans)
