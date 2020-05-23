class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        al,bl = 0,0
        
        while al < len(A) and bl < len(B):
            intersect_start, intersect_end = max(A[al][0], B[bl][0]), min(A[al][1], B[bl][1])
            
            if intersect_end >= intersect_start:
                ans.append([intersect_start, intersect_end])
                
                al, bl = al + (1 if A[al][1] <= B[bl][1] else 0), bl + (1 if B[bl][1] <= A[al][1] else 0)
            else:
                if A[al][0] < B[bl][0]: al += 1
                else: bl += 1
                    
        return ans
