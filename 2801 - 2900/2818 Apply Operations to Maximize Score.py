class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        m = max(nums)
        spf = [-1]*(m+1)
        ps = []

        for num in range(2,m+1):
            if spf[num] == -1:
                spf[num] = num
                ps.append(num)

            for p in ps:
                if p*num >= len(spf): break
                spf[p*num] = p

        fs = {}

        for num in set(nums):
            fs2 = set()
            num2 = num

            while num2 != 1:
                fs2.add(spf[num2])
                num2 //= spf[num2]

            fs[num] = len(fs2)

        l = []
        s = []

        for i,num in enumerate(nums):
            while s and fs[nums[s[-1]]] < fs[num]: s.pop()
            l.append(-1 if not s else s[-1])
            s.append(i)

        r = []
        s = []

        for i in range(len(nums)-1,-1,-1):
            while s and fs[nums[s[-1]]] <= fs[nums[i]]: s.pop()
            r.append(len(nums) if not s else s[-1])
            s.append(i)

        r.reverse()
        ans = 1

        for num,i,l2,r2 in sorted(zip(nums,range(len(nums)),l,r),reverse=True):
            use = min(k,(i-l2)*(r2-i))
            k -= use
            ans *= pow(num,use,mod)
            ans %= mod

        return ans
