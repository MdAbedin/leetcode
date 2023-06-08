class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums_set = set(arr)

        def solve(a,b):
            ans = 2
            
            while a+b in nums_set:
                a,b = b,a+b
                ans += 1

            return ans if ans >= 3 else 0

        return max(solve(arr[i],arr[j]) for i in range(len(arr)) for j in range(i+1,len(arr)))
