class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(l,r):
            if l >= r: return

            m = (l+r)//2
            merge_sort(l,m)
            merge_sort(m+1,r)

            merged = []
            li,ri = l,m+1

            while li <= m and ri <= r:
                if nums[li] <= nums[ri]:
                    merged.append(nums[li])
                    li += 1
                else:
                    merged.append(nums[ri])
                    ri += 1

            nums[l:r+1] = merged + nums[li:m+1] + nums[ri:r+1]

        merge_sort(0,len(nums)-1)

        return nums
