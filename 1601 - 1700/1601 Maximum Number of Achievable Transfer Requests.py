class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        
        for mask in range(2**len(requests)):
            d = [0]*n

            for i in range(len(requests)):
                if mask & (1<<i):
                    d[requests[i][0]] -= 1
                    d[requests[i][1]] += 1

            if set(d) == {0}: ans = max(ans, f"{mask:b}".count("1"))

        return ans
