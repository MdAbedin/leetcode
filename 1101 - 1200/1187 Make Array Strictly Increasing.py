class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def solve(i,prev):
            if i == len(arr1): return 0

            ans = inf if arr1[i] <= prev else solve(i+1,arr1[i])
            if (j := bisect_right(arr2,prev)) in range(len(arr2)): ans = min(ans, 1+solve(i+1,arr2[j]))

            return ans

        return -1 if (ans := solve(0,-inf)) == inf else ans
