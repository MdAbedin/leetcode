class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max((str(d)*3 for d in range(10) if str(d)*3 in num),default="")
