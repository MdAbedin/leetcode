class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        spf = [-1]*(right+1)
        primes = []

        for num in range(2,right+1):
            if spf[num] == -1:
                spf[num] = num
                primes.append(num)

            for prime in primes:
                if prime*num >= len(spf): break
                spf[prime*num] = prime

        ans = [inf,-1,-1]

        for p1,p2 in pairwise(primes):
            if not (left <= p1 and p2 <= right): continue
            ans = min(ans,[p2-p1,p1,p2])

        return ans[1:]
