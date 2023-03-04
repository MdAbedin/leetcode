class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        valid_subarrays = []
        cur_subarray = []

        for num in nums:
            if minK <= num <= maxK:
                cur_subarray.append(num)
            else:
                if cur_subarray: valid_subarrays.append(cur_subarray)
                cur_subarray = []

        if cur_subarray: valid_subarrays.append(cur_subarray)
        bounds = (minK,maxK)

        def solve(subarray):
            bound_counts = {minK:0,maxK:0}
            start = 0
            ans = 0

            for end,num in enumerate(subarray):
                if num in bounds: bound_counts[num] += 1

                while start < end and (subarray[start] not in bounds or bound_counts[subarray[start]] > 1):
                    if subarray[start] in bounds: bound_counts[subarray[start]] -= 1
                    start += 1

                if 0 not in bound_counts.values(): ans += start+1

            return ans

        return sum(map(solve, valid_subarrays))
