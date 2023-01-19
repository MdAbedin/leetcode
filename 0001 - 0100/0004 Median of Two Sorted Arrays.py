class Solution:
    """
    N1 = length of nums2
    N2 = length of nums2
    Time:  O(log^2(N1 * N2))
    Space: O(1)
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def rank_range(num):
            min_rank = bisect_left(nums1, num) + bisect_left(nums2, num)
            max_rank = total_len-1 - (len(nums1)-bisect_right(nums1, num) + len(nums2)-bisect_right(nums2, num))

            return min_rank, max_rank
        
        def find_rank(k):
            for nums in (nums1,nums2):
                l,r = 0,len(nums)-1
                
                while l <= r:
                    m = (l+r)//2
                    min_rank, max_rank = rank_range(nums[m])
                    
                    if k < min_rank: r = m-1
                    elif k > max_rank: l = m+1
                    else: return nums[m]
            
        total_len = len(nums1) + len(nums2)
        
        return (find_rank((total_len-1)//2) + find_rank(total_len//2)) / 2
    
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
                max_rank = total_len-1 - (len(nums1)-bisect_right(nums1, num) + len(nums2)-bisect_right(nums2, num))
                return max_rank >= k
            
            return -10**6 + bisect_left(range(-10**6,10**6+1), True, key = rank_k_or_greater)
        
        total_len = len(nums1) + len(nums2)
        
        return (find_rank((total_len-1)//2) + find_rank(total_len//2)) / 2
