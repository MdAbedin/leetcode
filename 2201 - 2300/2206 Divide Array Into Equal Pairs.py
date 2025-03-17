class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return set(map(partial(and_,1),Counter(nums).values())) == {0}
