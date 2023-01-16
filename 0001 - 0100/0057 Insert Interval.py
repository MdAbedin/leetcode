class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insort_left(intervals, newInterval)
        ans = []
        
        for s,e in intervals:
            if ans and s <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s,e])
            
        return ans
