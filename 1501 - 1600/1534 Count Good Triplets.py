class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[j]-arr[i]) <= a and abs(arr[k]-arr[j])<=b and abs(arr[k]-arr[i]) <= c:
                        ans += 1
                        
        return ans
