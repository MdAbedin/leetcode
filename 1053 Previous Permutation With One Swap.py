class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        min_num = A[-1]
        swap_index = len(A)-1
        
        for i in range(len(A)-2,-1,-1):
            if min_num < A[i]:
                swap_index = i
                break
                
            min_num = min(min_num, A[i])
            
        max_num = -1
        swap_index2 = swap_index
        
        for i in range(swap_index+1, len(A)):
            if A[i] < A[swap_index]:
                if A[i] > max_num:
                    max_num = A[i]
                    swap_index2 = i
                    
        A[swap_index], A[swap_index2] = A[swap_index2], A[swap_index]
        
        return A
