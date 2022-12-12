class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        locs = defaultdict(list)
        
        for i in range(len(nums)):
            locs[nums[i]].append(i)
            
        ans = []
        
        for l,r in queries:
            last = None
            cur_ans = inf
            
            for num in range(1,101):
                j = bisect_left(locs[num], l)
                exists = j < len(locs[num]) and locs[num][j] <= r
                
                if exists:
                    if last is not None:
                        cur_ans = min(cur_ans, num-last)
                    last = num
                    
            ans.append(-1 if cur_ans == inf else cur_ans)
            
        return ans
