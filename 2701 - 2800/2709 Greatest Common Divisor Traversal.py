MAX_N = 10**5
spf = [0]*(MAX_N+1)
primes = []

for x in range(2,MAX_N+1):
    if spf[x] == 0:
        spf[x] = x
        primes.append(x)

    for p in primes:
        if p*x >= len(spf): break
        spf[p*x] = p

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if 1 in nums: return nums == [1]
        
        nums = set(nums)
        prime_factors = set()
        parents = {}
        
        def union(a,b):
            parents[find(a)] = find(b)
        
        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]
        
        for num in nums:
            cur_prime_factors = set()
            
            while spf[num] != 0:
                cur_prime_factors.add(spf[num])
                if spf[num] not in parents: parents[spf[num]] = spf[num]
                num //= spf[num]

            for a,b in pairwise(cur_prime_factors): union(a,b)
            prime_factors |= cur_prime_factors 
            
        return len(set(map(find,prime_factors))) == 1
