class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        conflicts = [0]*(10**6+1)

        for s,e in intervals:
            conflicts[s] += 1
            conflicts[e] -= 1

        return max(accumulate(conflicts))
