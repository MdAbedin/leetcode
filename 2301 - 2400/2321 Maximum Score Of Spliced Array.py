class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        psums1, psums2 = [0]+list(accumulate(nums1)), [0]+list(accumulate(nums2))
        max_add1,max_add2 = 0,0
        max_ldiff1,max_ldiff2 = 0,0

        for psum1,psum2 in zip(psums1,psums2):
            max_add1 = max(max_add1,psum2-psum1 + max_ldiff1)
            max_add2 = max(max_add2,psum1-psum2 + max_ldiff2)
            
            max_ldiff1 = max(max_ldiff1, psum1-psum2)
            max_ldiff2 = max(max_ldiff2, psum2-psum1)

        return max(sum(nums1)+max_add1, sum(nums2)+max_add2)
