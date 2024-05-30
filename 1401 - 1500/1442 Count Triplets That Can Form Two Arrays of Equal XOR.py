class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        xor = 0
        inds = defaultdict(list,{0:[-1]})

        for i,x in enumerate(arr):
            xor ^= x
            ans += sum(i-i2-1 for i2 in inds[xor])
            inds[xor].append(i)

        return ans
