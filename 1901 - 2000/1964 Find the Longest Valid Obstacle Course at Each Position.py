class Solution:

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        ends = [-inf] + [inf]*len(obstacles)

        ans = []

        

        for height in obstacles:

            i = bisect_right(ends,height)

            ans.append(i)

            ends[i] = height

        

        return ans
