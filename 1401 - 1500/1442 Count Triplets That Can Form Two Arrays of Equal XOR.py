class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        xor = 0
        data = defaultdict(lambda:[0,0],{0:[0,1]})

        for i,x in enumerate(arr):
            xor ^= x
            ans += i*data[xor][1]-data[xor][0]
            data[xor][0] += i+1
            data[xor][1] += 1

        return ans
