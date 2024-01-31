class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while s and s[-1][1] < t: ans[i2] = i-(i2 := s.pop()[0])
            s.append((i,t))

        return ans
