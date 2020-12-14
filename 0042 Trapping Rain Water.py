class Solution:
    def trap(self, height: List[int]) -> int:
        ls, rs = [], []
        for i in range(len(height)):
            ls.append(max(height[i], ls[-1] if ls else -1))
            rs.append(max(height[-1*i-1], rs[-1] if rs else -1))
        rs = rs[::-1]
        ans = 0
        
        for i in range(len(height)):
            ans += min(ls[i], rs[i])-height[i]
        return ans
