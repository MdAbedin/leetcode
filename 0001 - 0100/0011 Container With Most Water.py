class Solution:
    def maxArea(self, height: List[int]) -> int:
        indexes = defaultdict(list)
        for i,h in enumerate(height): indexes[h].append(i)
        ans = 0
        l,r = inf,-inf

        for container_height in range(10**4,0,-1):
            for i in indexes[container_height]:
                l = min(l,i)
                r = max(r,i)

            ans = max(ans, container_height*(r-l))

        return ans
