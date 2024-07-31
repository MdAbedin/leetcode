class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def solve(i):
            if i == len(books): return 0
            
            ans = inf
            w = 0
            h = 0

            for i2 in range(i,len(books)):
                w += books[i2][0]
                h = max(h,books[i2][1])
                if w > shelfWidth: break
                ans = min(ans,h+solve(i2+1))

            return ans

        return solve(0)
