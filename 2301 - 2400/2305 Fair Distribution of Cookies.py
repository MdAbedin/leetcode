class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf

        for initial_distribution in permutations(cookies,k):
            bags_left = cookies[:]
            for bag in initial_distribution: bags_left.remove(bag)
            
            for mask in range(k**(len(cookies)-k)):
                dist = list(initial_distribution)

                for i in range(len(cookies)-k):
                    dist[mask%k] += bags_left[i]
                    mask //= k

                ans = min(ans,max(dist))

        return ans
