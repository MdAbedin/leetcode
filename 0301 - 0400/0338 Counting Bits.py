class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)

        for num in range(n+1): ans[num] = ans[num//2]+(num%2)
        
        return ans
