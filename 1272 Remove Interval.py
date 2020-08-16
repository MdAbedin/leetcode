class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        l, r = toBeRemoved
        
        for l2, r2 in intervals:
            if l <= l2 and r >= r2:
                continue
            elif l > l2 and r < r2:
                ans.append([l2, l])
                ans.append([r, r2])
            elif l > l2 and l < r2:
                ans.append([l2, l])
            elif r < r2 and r > l2:
                ans.append([r, r2])
            else:
                ans.append([l2,r2])
            
        return ans
