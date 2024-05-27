class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ans = bisect_left(range(101),True,key=lambda x: sum(map(partial(le,x),nums)) <= x)
        return -1 if sum(map(partial(le,ans),nums)) != ans else ans
