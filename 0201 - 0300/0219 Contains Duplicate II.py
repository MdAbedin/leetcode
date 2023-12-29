class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        inds = defaultdict(list)
        for i,num in enumerate(nums): inds[num].append(i)
        return any(i2-i1 <= k for inds2 in inds.values() for i1,i2 in pairwise(inds2))
