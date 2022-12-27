class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        return all(a[1] <= b[0] for a,b in zip(sorted(intervals), sorted(intervals)[1:]))
