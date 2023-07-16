class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = Counter(nums)
        d = max(c,key=c.__getitem__)
        lc,rc = Counter(),c
        
        for i in range(len(nums)-1):
            num = nums[i]
            lc[num] += 1
            rc[num] -= 1
            if lc[d] > (i+1)/2 and rc[d] > (len(nums)-i-1)/2: return i
        
        return -1
