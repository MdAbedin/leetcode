class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def works(k):
            subs = [0]*(len(nums)+1)
    
            for l,r,v in queries[:k]:
                subs[l] += v
                subs[r+1] -= v
    
            return all(starmap(le,zip(nums,accumulate(subs))))

        return -1 if (ans := bisect_left(range(len(queries)+1),True,key=works)) == len(queries)+1 else ans
