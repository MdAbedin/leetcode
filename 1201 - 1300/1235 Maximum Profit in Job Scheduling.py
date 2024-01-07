class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ints = sorted(zip(startTime,endTime,profit),key = lambda l: l[1])
        ans = [(0,0)]

        for s,e,p in ints:
            p2 = ans[bisect_right(ans,(s,inf))-1][1]+p
            if p2 > ans[-1][1]: ans.append((e,p2))

        return ans[-1][1]
