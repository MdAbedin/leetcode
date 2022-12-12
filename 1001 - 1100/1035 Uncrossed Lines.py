class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        buf = [0]*len(A)
        
        for i in range(len(B)):
            buf2 = [0]*len(A)
            
            for j in range(len(A)):
                buf2[j] = max(buf2[j-1] if j-1>=0 else 0, buf[j], (buf[j-1] if j-1>= 0 else 0) + 1 if A[j]==B[i] else 0)
                
            buf = buf2
            
        return buf[-1]
