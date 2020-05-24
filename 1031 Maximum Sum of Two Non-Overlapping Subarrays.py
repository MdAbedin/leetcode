class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        L_sums = A[::]
        
        for i in range(1,len(L_sums)):
            L_sums[i] += L_sums[i-1] - (A[i-L] if i-L>=0 else 0)
                
        M_info = [[num]*3 for num in A]
        
        for i in range(1,len(M_info)):
            M_info[i][0] += M_info[i-1][0] - (A[i-M] if i-M>=0 else 0)
            M_info[i][1] = max(M_info[i-1][1], M_info[i][0])
            
        for i in range(len(A)-M, -1, -1):
            M_info[i][2] = max(M_info[i+1][2] if i+1<len(A) else A[i], M_info[i+M-1][0])
            
        ans = 0
        
        for i in range(L-1, len(L_sums)):
            ans = max(ans, L_sums[i] + max(M_info[i-L][1] if i-L>= 0 else 0, M_info[i+1][2] if i+1 < len(A) else 0))
            
        return ans
