class Solution:
    """
    R = size of range of integers in nums1 and nums2
    N1 = length of nums2
    N2 = length of nums2
    Time:  O(log(R) * (log(N1) + log(N2)))
    Space: O(1)
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        def find_rank(k):
            def rank_k_or_greater(num):
                min_rank = bisect_left(nums1, num) + bisect_left(nums2, num)
                max_rank = total_len-1 - (len(nums1)-bisect_right(nums1, num) + len(nums2)-bisect_right(nums2, num))
                
                return min_rank > k or max_rank >= k
            
            return -10**6 + bisect_left(range(-10**6,10**6+1), True, key = rank_k_or_greater)
        
        total_len = len(nums1) + len(nums2)
        
        return (find_rank(total_len//2-1 + total_len%2) + find_rank(total_len//2)) / 2
