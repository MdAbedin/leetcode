class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags = defaultdict(deque)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i+j].appendleft(nums[i][j])
        
        ans = []
        for key in sorted(diags.keys()):
            for n in diags[key]:
                ans.append(n)
                
        return ans
