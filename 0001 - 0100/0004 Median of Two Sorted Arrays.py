class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        
        if total_len == 1: return (nums1 + nums2)[0]
        if total_len == 2: return (sum(nums1) + sum(nums2)) / 2
        
        def find_rank(k):
            def rank_k_or_greater(num):
                min_rank = bisect_left(nums1, num) + bisect_left(nums2, num)
                max_rank = total_len-1 - (len(nums1)-bisect_right(nums1, num) + len(nums2)-bisect_right(nums2, num))
                
                return min_rank > k or max_rank >= k
            
            return -10**6 + bisect_left(range(-10**6,10**6+1), True, key = rank_k_or_greater)
        
        if total_len%2 == 1:
            return find_rank(total_len//2)
        else:
            return (find_rank(total_len//2-1) + find_rank(total_len//2)) / 2
