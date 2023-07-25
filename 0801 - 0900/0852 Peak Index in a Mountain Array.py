class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr)-1

        while l <= r:
            m = (l+r)//2

            if m-1 >= 0 and m+1 < len(arr) and arr[m-1] < arr[m] > arr[m+1]: return m

            if m == 0 or arr[m-1] < arr[m]: l = m+1
            else: r = m-1
