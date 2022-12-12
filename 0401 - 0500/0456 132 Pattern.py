class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        lefts = [None]
        mn = nums[0]
        
        for i in range(1,len(nums)):
            lefts.append(mn if mn < nums[i] else None)
            mn = min(mn, nums[i])
        
        rights = [None]*len(nums)
        nums_sorted = sorted([[nums[i], i] for i in range(len(nums))], reverse=True)
        unmatched = []
        
        for num,i in nums_sorted:
            while unmatched and unmatched[0] < i:
                rights[heappop(unmatched)] = num
                
            heappush(unmatched, i)
        
        return any(lefts[i] is not None and rights[i] is not None and lefts[i]<rights[i]<nums[i] for i in range(len(nums)))
