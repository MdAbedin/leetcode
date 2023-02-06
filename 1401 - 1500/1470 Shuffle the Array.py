class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for num in chain.from_iterable(zip(islice(nums,n), islice(nums,n,2*n)))]
