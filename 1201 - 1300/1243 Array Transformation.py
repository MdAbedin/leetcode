class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            new_arr = [arr[0]] + [arr[i] + (1 if arr[i-1]>arr[i]<arr[i+1] else (-1 if arr[i-1]<arr[i]>arr[i+1] else 0)) for i in range(1,len(arr)-1)] + [arr[-1]]
            if new_arr == arr: break
            arr = new_arr

        return arr
