class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        nexts = defaultdict(list)

        for prev,nxt in relations: nexts[prev].append(nxt)

        @cache
        def solve(course): return time[course-1] + max(map(solve,nexts[course]),default=0)

        return max(map(solve,range(1,n+1)))
